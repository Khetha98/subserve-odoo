{
    'name': 'Subserve Compliance',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'CIPC & SARS Compliance Documents',
    'depends': ['base'],
    'data': [
            'security/ir.model.access.csv',
            'data/compliance_defaults.xml',
            'views/company_views.xml',
            'views/compliance_action.xml',   # Define the actions first
            'views/compliance_views.xml',    # Define the views
            'views/add_compliance_data.xml', # If the action is here, move it up!
            'views/compliance_menu.xml',     # Menus should almost always be LAST
            'reports/cipc_report.xml',
            'reports/cipc_report_action.xml',
        ],
    'installable': True,
    'application': True,
}
