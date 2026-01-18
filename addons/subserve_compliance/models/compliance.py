from odoo import models, fields

class SubserveCompliance(models.Model):
    _name = 'subserve.compliance'
    _description = 'Subserve Compliance Record'

    name = fields.Char(required=True)
    status = fields.Selection([
        ('valid', 'Valid'),
        ('expired', 'Expired'),
        ('pending', 'Pending'),
        ('submitted', 'Submitted to CIPC'),
    ], default='pending')
    
    # New fields for CIPC requirements
    is_fas_required = fields.Boolean(string="FAS Required", default=True, help="Financial Accountability Supplement")
    beneficial_ownership_filed = fields.Boolean(string="Beneficial Ownership Filed")
    reference_number = fields.Char(string="CIPC Reference")
    
    expiry_date = fields.Date(string="Deadline")
    company_id = fields.Many2one('res.company', string='Company', required=True)
    is_audited = fields.Boolean(string="Is Audited/Reviewed", default=False, help="If NO, the CIPC Compliance Checklist is not required.")

    def action_mark_as_filed(self):
        for record in self:
            record.status = 'valid'
            # Update the company-level boolean you created earlier
            record.company_id.compliance_document_ready = True