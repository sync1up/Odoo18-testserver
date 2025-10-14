# -*- coding: utf-8 -*-
{
    'name': 'ChatGPT Browser',
    'version': '1.0.0',
    'category': 'Tools',
    'summary': 'Launch ChatGPT browser window from Odoo',
    'description': """        ChatGPT Browser Integration
        ============================

        Launch a dedicated ChatGPT browser window directly from Odoo.

        Features:
        ---------
        * Launch ChatGPT in standalone browser window
        * User-specific sessions
        * PyQt6-based browser integration

        Requirements:
        -------------
        * PyQt6
        * PyQt6-WebEngine

        Installation:
        -------------
        1. Upload this module to your Odoo addons directory
        2. Install dependencies: pip3 install -r requirements.txt
        3. Restart Odoo
        4. Install module via Apps menu
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'license': 'LGPL-3',
    'depends': ['base'],
    'external_dependencies': {
        'python': ['PyQt6', 'PyQt6.QtWebEngineWidgets'],
    },
    'data': [
        'security/ir.model.access.csv',
        'views/chatgpt_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
