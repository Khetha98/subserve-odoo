from odoo import models, api

@api.model
def _check_cash_risk(self, order):
    cash_total = sum(
        p.amount for p in order.payment_ids
        if p.payment_method_id.is_cash
    )

    if cash_total >= 100000:
        self.env['subserve.compliance.issue'].create({
            'company_id': order.company_id.id,
            'issue': 'High-value CASH transaction',
            'severity': 'high',
            'source_model': 'pos.order',
            'source_id': order.id,
        })

