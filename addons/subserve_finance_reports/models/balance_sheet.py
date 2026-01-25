from odoo import models, fields, api

class BalanceSheetReport(models.TransientModel):
    _name = 'subserve.balance.sheet.wizard'
    _description = 'Balance Sheet Wizard'

    date_to = fields.Date(required=True)

    def get_lines(self):
        lines = self.env['account.move.line'].read_group(
            domain=[
                ('date', '<=', self.date_to),
                ('account_id.account_type', 'in',
                 ['asset', 'liability', 'equity']),
                ('move_id.state', '=', 'posted')
            ],
            fields=['debit', 'credit'],
            groupby=['account_id']
        )

        result = []
        for l in lines:
            balance = l['debit'] - l['credit']
            result.append({
                'account': l['account_id'][1],
                'balance': balance,
            })
        return result
    
    def action_print(self):
        return self.env.ref(
            'subserve_finance_reports.balance_sheet_pdf'
        ).report_action(self)

