{
    'name': 'Subserve Finance Reports',
    'version': '1.0.0',
    'category': 'Accounting',
    'summary': 'Community financial statements (Balance Sheet, P&L, Cash Flow)',
    'depends': ['account', 'web'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/finance_report_wizards.xml',
        'views/finance_report_menu.xml',
        'reports/balance_sheet.xml',
        'reports/income_statement.xml',
        'reports/cash_flow.xml',
        'reports/reconciliation.xml',
    ],
    'installable': True,
    'application': True,
}
