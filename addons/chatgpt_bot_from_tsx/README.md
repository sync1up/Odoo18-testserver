# ChatGPT Browser Module voor Odoo

## Beschrijving
Deze module maakt het mogelijk om een ChatGPT browser window te openen vanuit Odoo.

## Installatie

### Stap 1: Module uploaden
Plaats de `chatgpt_bot` folder in je Odoo addons directory:
```
/opt/odoo/addons/chatgpt_bot/
```

### Stap 2: Dependencies installeren
```
cd /opt/odoo/addons/chatgpt_bot/
pip3 install -r requirements.txt
```

### Stap 3: Odoo herstarten
```
sudo systemctl restart odoo
# of
sudo service odoo restart
```

### Stap 4: Module activeren
1. Log in op Odoo als administrator
2. Ga naar Apps menu
3. Verwijder het "Apps" filter
4. Zoek naar "ChatGPT Browser"
5. Klik op "Install"

## Gebruik
1. Ga naar het ChatGPT menu in Odoo
2. Klik op "Launch ChatGPT Browser"
3. Een nieuw browser window wordt geopend met ChatGPT

## Troubleshooting

### PyQt6 niet gevonden
Als je deze fout krijgt bij het installeren van de module:
```
PyQt6 is not installed on this system
```

Oplossing:
```
pip3 install PyQt6 PyQt6-WebEngine
```

### Browser opent niet
Check de Odoo logs:
```
tail -f /var/log/odoo/odoo.log
```

## Technische Details
- **Python Dependencies**: PyQt6, PyQt6-WebEngine
- **Odoo Version**: 14.0+ (compatible met 15, 16, 17)
- **License**: LGPL-3
