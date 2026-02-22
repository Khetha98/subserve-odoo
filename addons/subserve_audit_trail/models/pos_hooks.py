from odoo import models, api

class PosOrder(models.Model):
    _inherit = 'pos.order'

    @api.model
    def create(self, vals):
        order = super().create(vals)

        self.env['subserve.audit.log'].create({
            'source_model': 'pos.order',
            'source_id': order.id,
            'action': 'POS Order Created',
            'amount': order.amount_total,
        })

        return order
