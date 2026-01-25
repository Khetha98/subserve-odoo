from odoo import models, fields, api

class CashFlowReport(models.TransientModel):
    _name = 'subserve.cash.flow.wizard'
    _description = 'Cash Flow Wizard'

    date_from = fields.Date(required=True)
    date_to = fields.Date(required=True)

    def get_lines(self):
        return self.env['account.move.line'].search([
            ('journal_id.type', 'in', ['cash', 'bank']),
            ('date', '>=', self.date_from),
            ('date', '<=', self.date_to),
            ('move_id.state', '=', 'posted'),
        ])
