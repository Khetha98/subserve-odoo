# models/pos_order.py
from odoo import models

class PosOrder(models.Model):
    _inherit = 'pos.order'

    def action_pos_order_paid(self):
        res = super().action_pos_order_paid()

        for order in self:
            company = order.company_id
            # Example compliance flag
            company.compliance_document_ready = False

        return res
