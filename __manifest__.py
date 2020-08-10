# -*- coding: utf-8 -*-
{
    'name': "Odoo Simple API",

    'summary': """
        This module is create for CRUD API""",

    'description': """
        This module is very simple CRUD API that i create for all Odoo developer 
        I Hope it helpful to all of you
    """,

    'author': "PANG-SORAM-DEPO",
    'website': "https://github.com/PangSoramDepo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}