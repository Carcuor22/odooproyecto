# -*- coding: utf-8 -*-
{
    'name': "odooproyecto",

    'summary': """
       Aplicacion Odoo para gestionar un taller de coches""",

    'description': """
        Aplicacion Odoo para gestionar un taller de coches
    """,

    'author': "HM",
    'website': "http://ieshnosmachado.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/taller_view.xml',
        'views/menu_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
