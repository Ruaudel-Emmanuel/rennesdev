<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Hier, on a parlé ensemble et qui m'a fait un Un descriptif de la manière sous sous serveur VPS. Comment modifier le Le prix dans payments . py

Oui. Dans ton cas, le prix se modifie directement dans `payments.py`, sur la variable `SESSION_CONSEIL_PRICE`, puis il faut redémarrer le service API pour que le changement soit pris en compte.[^1][^2]

## Fichier à modifier

Le backend actif tourne depuis `/home/manu/var/www/api-rennesdev-backend`, et le fichier à éditer est `app/api/v1/payments.py`.[^3]

Commande :

```bash
nano /home/manu/var/www/api-rennesdev-backend/app/api/v1/payments.py
```


## Ligne à changer

La consigne qu’on avait fixée hier était de remplacer la valeur actuelle par `14900`, ce qui correspond à 149 € HT si ton code attend un montant en centimes.[^1]

Cherche cette ligne :

```python
SESSION_CONSEIL_PRICE = 5000
```

Remplace par :

```python
SESSION_CONSEIL_PRICE = 14900
```


## Redémarrage

Après sauvegarde, redémarre le service `api-rennesdev` pour recharger le code Python modifié.[^2][^1]

```bash
sudo systemctl restart api-rennesdev
```

Tu peux vérifier ensuite :

```bash
sudo systemctl status api-rennesdev
```


## Vérification utile

Si le bouton HTML affiche aussi un prix, il faut penser à modifier les deux côtés : le front visible par le client et la valeur backend dans `payments.py`, sinon tu risques d’afficher un prix et d’en facturer un autre.[^1]

Version ultra courte à exécuter :

```bash
nano /home/manu/var/www/api-rennesdev-backend/app/api/v1/payments.py
# remplacer SESSION_CONSEIL_PRICE par 14900
sudo systemctl restart api-rennesdev
```

Tu veux que je te redonne aussi la commande pour retrouver automatiquement la ligne exacte avec `grep` avant modification ?
<span style="display:none">[^10][^11][^12][^13][^14][^15][^16][^17][^4][^5][^6][^7][^8][^9]</span>

<div align="center">⁂</div>

[^1]: https://www.perplexity.ai/search/b85e0786-2093-47e3-9db2-acde906d2b54

[^2]: https://alexhost.com/fr/faq/systemctl-commands-restart-reload-and-stop-service-in-linux/

[^3]: https://www.perplexity.ai/search/4de6b58a-12fc-4e60-9b53-30ebfa143c64

[^4]: https://help.one.com/hc/fr/articles/26410277928593-Comment-gérer-et-ajuster-les-ressources-et-les-plans-VPS

[^5]: https://werobot.fr/blog/demarrer-un-script-python-au-moment-du-boot-d-un-raspberry-pi-4-avec-un-service-systemd/

[^6]: https://www.reddit.com/r/linuxquestions/comments/1fq7lbl/systemd_command_to_reboot_in_x_minutes/

[^7]: https://www.reddit.com/r/django/comments/1p448vd/uvicorn_service_fails_to_restart_after_reboot/

[^8]: https://paiement.systempay.fr/doc/fr-FR/faq/ec/modifier-l-ordre-d-affichage-des-moyens-de-paiement-a-l-acheteur-sur-prestashop.html

[^9]: https://www.reddit.com/r/linuxquestions/comments/saa4ip/need_help_running_python_script_as_service_ubuntu/

[^10]: https://www.debian-fr.org/t/erreur-too-few-arguments-debutant-debutant/86814

[^11]: https://uvicorn.dev/settings/

[^12]: https://supply.getyourguide.support/hc/fr-fr/articles/23699860932125-Modifier-vos-informations-de-paiement-dans-l-Espace-prestataire

[^13]: https://anderson69s.com/2016/10/19/python-systemd/

[^14]: https://www.developpez.net/forums/d2152351/systemes/linux/commande-python-pilotage-machine-linux/

[^15]: https://stackoverflow.com/questions/52784924/problem-enabling-uvicorn-auto-restart-when-launching-programmatically-with-uvico

[^16]: https://www.reddit.com/r/OVHcloud/comments/1u1bxa0/payment_debited_but_dashboard_says_not_received/

[^17]: https://linuxfr.org/forums/linux-general/posts/systemd-et-ordre-de-demarrage

