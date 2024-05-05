{
    'name': 'Barangay Management Information System',
    'summary': """Government Resource Planning for Barangay""",
    'description': """Barangay MIS developed by Infinion APAC - this is for demo purpose only.
        """,
    'license': 'OPL-1',
    'author': 'Gigio89',
    'website': 'www.infinion.group',
    'category': 'Custom Modules/eGovernance',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/bmis_groups.xml',
        'security/ir.model.access.csv',
        'security/bmis_security.xml',
        'views/bmis_menuitems.xml',
        'views/resident_views.xml',
    ],
        
    'demo': [
       
    ],
    'application': True,
}
