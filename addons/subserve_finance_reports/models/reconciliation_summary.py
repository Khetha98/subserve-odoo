from odoo import models, fields, api

class ReconciliationSummary(models.TransientModel):
    _name = 'subserve.reconciliation.wizard'
    _description = 'Reconciliation Summary'

    date_to = fields.Date(required=True)

    def get_unreconciled(self):
        return self.env['account.move.line'].search([
            ('reconciled', '=', False),
            ('account_id.reconcile', '=', True), # Only accounts that allow reconciliation
            ('date', '<=', self.date_to),
            ('move_id.state', '=', 'posted')
        ])

    def action_print(self):
        return self.env.ref(
            'subserve_finance_reports.reconciliation_pdf'
        ).report_action(self)
