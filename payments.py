import stripe
import httpx
from fastapi import APIRouter, HTTPException, Request, Header
from fastapi.responses import JSONResponse
from app.core.config import settings
from app.core.logging import get_logger

logger = get_logger("app.api.v1.payments")
router = APIRouter(prefix="/payments", tags=["payments"])

SESSION_CONSEIL_NAME     = "Session Conseil Automatisation – 1h en visio"
SESSION_CONSEIL_PRICE    = 14900  # centimes = 149,00 €
SESSION_CONSEIL_CURRENCY = "eur"

@router.post("/session-conseil")
async def create_checkout_session(request: Request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    origin = request.headers.get("origin", "https://rennesdev.fr")
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price_data": {
                    "currency": SESSION_CONSEIL_CURRENCY,
                    "unit_amount": SESSION_CONSEIL_PRICE,
                    "product_data": {
                        "name": SESSION_CONSEIL_NAME,
                        "description": "Visio 1h · Identification de vos automatisations · Compte-rendu inclus",
                    },
                },
                "quantity": 1,
            }],
            mode="payment",
            success_url=f"{origin}/merci.html?session_id={{CHECKOUT_SESSION_ID}}",
            cancel_url=f"{origin}/Session-Conseil-Automatisation.html",
            tax_id_collection={"enabled": True},
            invoice_creation={"enabled": True},
            metadata={"product": "session-conseil"},
        )
        logger.info(f"Checkout Session créée : {session.id}")
        return {"checkout_url": session.url}
    except stripe.StripeError as e:
        raise HTTPException(status_code=502, detail=f"Stripe error: {e.user_message}")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erreur serveur")


@router.post("/webhook")
async def stripe_webhook(
    request: Request,
    stripe_signature: str = Header(None, alias="stripe-signature"),
):
    payload = await request.body()
    try:
        event = stripe.Webhook.construct_event(
            payload, stripe_signature, settings.STRIPE_WEBHOOK_SECRET
        )
    except stripe.errors.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")
    except Exception:
        raise HTTPException(status_code=400, detail="Webhook error")

    if event["type"] == "checkout.session.completed":
        s = event["data"]["object"]
        customer_email = s.get("customer_details", {}).get("email", "")
        customer_name  = s.get("customer_details", {}).get("name", "")
        amount_total   = s.get("amount_total", 0) / 100
        session_id     = s.get("id", "")

        logger.info(f"Paiement confirmé : {customer_email} – {session_id}")

        if settings.N8N_ORDERS_WEBHOOK_URL:
            try:
                async with httpx.AsyncClient(timeout=10) as client:
                    await client.post(settings.N8N_ORDERS_WEBHOOK_URL, json={
                        "event":          "session_conseil_paid",
                        "session_id":     session_id,
                        "customer_email": customer_email,
                        "customer_name":  customer_name,
                        "amount":         amount_total,
                        "currency":       "EUR",
                        "product":        "session-conseil",
                    })
            except Exception as e:
                logger.error(f"Erreur n8n : {e}")

    return JSONResponse(content={"status": "ok"})