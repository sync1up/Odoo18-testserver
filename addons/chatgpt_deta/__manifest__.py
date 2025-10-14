{
    'name': 'ChatGPT DETA',
    'version': '18.0.1.0.0',
    'category': 'Productivity',
    'summary': 'Open ChatGPT DETA in new tab',
    'description': """
        ChatGPT DETA Link
        =================
        Simple menu item that opens ChatGPT DETA in a new browser tab.
    """,
    'author': 'Your Company',
    'depends': ['base', 'web'],
    'data': [
        'views/chatgpt_menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}