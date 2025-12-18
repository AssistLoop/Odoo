# -*- coding: utf-8 -*-
{
    'name': 'AssistLoop AI Chatbot',
    'version': '19.0.1.0.0',
    'category': 'Website',
    'summary': 'Integrate AssistLoop AI-powered chat widget into your Odoo website',
    'description': """
AssistLoop AI Chatbot for Odoo
==============================

Integrate the AssistLoop AI-powered customer support chatbot into your Odoo website.

Features
--------
* Easy configuration through Website Settings
* Enable/disable chatbot with one click
* AI-powered customer support 24/7
* Human handoff when needed
* Compatible with Odoo 19.0

Configuration
-------------
1. Go to Website → Configuration → Settings
2. Find the "AssistLoop AI Chatbot" section
3. Enter your Agent ID from AssistLoop dashboard
4. Enable the chatbot
5. Save settings

Requirements
------------
* Valid AssistLoop account (https://assistloop.ai)
* At least one configured AI agent in AssistLoop

Support
-------
For support, please contact support@assistloop.ai
    """,
    'author': 'AssistLoop',
    'website': 'https://assistloop.ai',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'website',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_config_parameter_data.xml',
        'views/res_config_settings_views.xml',
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'assistloop_odoo/static/src/js/assistloop_widget.js',
        ],
    },
    'images': [
        'static/description/icon.png',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
