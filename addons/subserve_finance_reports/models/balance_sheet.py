from odoo import models, fields, api

class BalanceSheetReport(models.TransientModel):
    _name = 'subserve.balance.sheet.wizard'
    _description = 'Balance Sheet Wizard'

    date_to = fields.Date(required=True)

    def get_lines(self):
        account_types = [
            'asset_receivable', 'asset_cash', 'asset_current', 'asset_non_current', 
            'asset_prepayments', 'asset_fixed', 'liability_payable', 
            'liability_credit_card', 'liability_current', 'liability_non_current',
            'equity', 'equity_unaffected'
        ]
        
        lines = self.env['account.move.line'].read_group(
            domain=[
                ('date', '<=', self.date_to),
                ('account_id.account_type', 'in', account_types),
                ('move_id.state', '=', 'posted'),
                ('display_type', 'not in', ('line_section', 'line_note'))
            ],
            fields=['debit', 'credit', 'account_id'],
            groupby=['account_id']
        )

        return [{
            'account': l['account_id'][1],
            'balance': l['debit'] - l['credit']
        } for l in lines]

    
    def action_print(self):
        return self.env.ref(
            'subserve_finance_reports.balance_sheet_pdf'
        ).report_action(self)

