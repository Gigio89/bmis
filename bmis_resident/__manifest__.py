# -*- coding: utf-8 -*-
{
    'name': "Barangay Household",

    'summary': "Module for all registered Barangay Residents",

    'description': """
Barangay MIS developed by Infinion APAC - this is for demo purpose only.
    """,
    'license': 'OPL-1',
    'author': "Infinion Group",
    'website': "https://www.infinion.group",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Custom Modules/eGovernment',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['bmis','contacts'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/bmis_resident_menuitems.xml',
        'views/res_partner_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        
    ],
    'auto_install':True,
    'application': True,
}

