{
    'name': 'OpenAI Chat (Native, no iframe)',
    'version': '18.0.1.0',
    'category': 'Productivity',
    'summary': 'Full-bleed ChatGPT-like chat inside Odoo using OpenAI API, per-user sessions',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/chat_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'openai_chat_native/static/src/js/chat_client.js',
            'openai_chat_native/static/src/scss/chat.scss',
        ],
    },
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}