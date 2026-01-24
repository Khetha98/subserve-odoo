from odoo import models

class DisableOdooCom(models.AbstractModel):
    _name = "disable.odoo.com"

    def _disable_links(self):
        self.env['ir.config_parameter'].sudo().set_param(
            'web.base.url.freeze', True
        )
