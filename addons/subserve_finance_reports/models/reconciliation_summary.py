from odoo import models, fields, api

class ReconciliationSummary(models.TransientModel):
    _name = 'subserve.reconciliation.wizard'
    _description = 'Reconciliation Summary'

    date_to = fields.Date(required=True)

    def get_unreconciled(self):
        return self.env['account.move.line'].search([
            ('reconciled', '=', False),
            ('date', '<=', self.date_to),
            ('move_id.state', '=', 'posted')
        ])
