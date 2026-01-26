from odoo import models, fields, api

class CashFlowReport(models.TransientModel):
    _name = 'subserve.cash.flow.wizard'
    _description = 'Cash Flow Wizard'

    date_from = fields.Date(required=True)
    date_to = fields.Date(required=True)

    def get_lines(self):
        lines = self.env['account.move.line'].read_group(
            domain=[
                ('journal_id.type', 'in', ['cash', 'bank']),
                ('date', '>=', self.date_from),
                ('date', '<=', self.date_to),
                ('move_id.state', '=', 'posted'),
            ],
            fields=['debit', 'credit', 'account_id'],
            groupby=['account_id'],
        )
        return [{
            'account': l['account_id'][1],
            'balance': l['debit'] - l['credit']
        } for l in lines]

    def action_print(self):
        return self.env.ref(
            'subserve_finance_reports.cash_flow_pdf'
        ).report_action(self)
