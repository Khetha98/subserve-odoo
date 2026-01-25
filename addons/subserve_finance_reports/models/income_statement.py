from odoo import models, fields, api

class IncomeStatementReport(models.TransientModel):
    _name = 'subserve.income.statement.wizard'
    _description = 'Income Statement Wizard'

    date_from = fields.Date(required=True)
    date_to = fields.Date(required=True)

    def get_lines(self):
        return self.env['account.move.line'].read_group(
            domain=[
                ('date', '>=', self.date_from),
                ('date', '<=', self.date_to),
                ('account_id.account_type', 'in', ['income', 'expense']),
                ('move_id.state', '=', 'posted'),
            ],
            fields=['debit', 'credit'],
            groupby=['account_id'],
        )
