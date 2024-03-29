# -*- coding: utf-8 -*-
{
    'name': "Saldo APP",

    'summary': """
        Aplicación para gestionar ingresos y egresos de multplies usuarios""",

    'description': """
        Aplicación para gestionar ingresos y egresos de multplies usuarios
    """,

    'author': "Escuela FULLSTACK",
    'website': "http://www.escuelafullstack.com",

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
        'views/perfil.xml',
        'views/views.xml',
        'views/templates.xml',
        'report/report_movimiento.xml',
        'report/report_movimiento_consolidado.xml',
        'report/reports.xml',
        'actions_server/validar_movimiento.xml',
        'security/res_groups.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}