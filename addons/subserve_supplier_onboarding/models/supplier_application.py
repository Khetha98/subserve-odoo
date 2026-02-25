# models/supplier_application.py
from odoo import models, fields

class SupplierApplication(models.Model):
    _name = 'subserve.supplier.application'
    _description = 'Supplier Application'

    name = fields.Char(required=True)
    email = fields.Char(required=True)
    phone = fields.Char()
    farm_name = fields.Char()
    product_types = fields.Text()
    status = fields.Selection([
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], default='pending')
    rejection_reason = fields.Text()