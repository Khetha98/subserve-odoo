from odoo import models, fields

class SubserveAuditLog(models.Model):
    _name = 'subserve.audit.log'
    _description = 'Audit Log'
    _order = 'timestamp desc'

    timestamp = fields.Datetime(default=fields.Datetime.now)
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user)
    source_model = fields.Char(required=True)
    source_id = fields.Integer(required=True)
    action = fields.Char(required=True)
    amount = fields.Monetary()
    currency_id = fields.Many2one(
        'res.currency',
        default=lambda self: self.env.company.currency_id
    )

    
