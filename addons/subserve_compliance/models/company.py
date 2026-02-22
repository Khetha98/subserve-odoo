from odoo import models, fields, api
from datetime import date


class ComplianceCompany(models.Model):
    _inherit = 'res.company'

    cipc_registration_no = fields.Char(string='CIPC Registration Number')
    vat_number = fields.Char(string='SARS VAT Number')
    compliance_document_ready = fields.Boolean(string='Compliance Document Ready', default=False)

    @api.model
    def create_default_compliance(self):
        """Create a default compliance record for every company if none exists"""
        current_year = date.today().year
        for company in self.search([]):
            existing = self.env['subserve.compliance'].search([
                ('name', '=', f"Annual Return {current_year}"),
                ('company_id', '=', company.id)
            ])
            if not existing:
                self.env['subserve.compliance'].create({
                    'name': f"Annual Return {current_year}",
                    'status': 'pending',
                    'expiry_date': date(current_year, 1, 28),
                    'company_id': company.id,
                })
