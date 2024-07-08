# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom_title(models.Model):
    _inherit = 'res.company'

    document_title = fields.Char("Document Title")

    title_in_pos_comp = fields.Boolean("Enable Custom Title in POS")

    def return_document_title(self):

        active_company = self.env.company.id
        active_company = self.env['res.company'].browse(active_company)      
        
        return active_company.document_title

class BdPOSModuleToggle(models.TransientModel):
    _inherit = 'res.config.settings'

    title_in_pos = fields.Boolean("Enable Custom Title in POS", store=True, related="company_id.title_in_pos_comp", readonly=False)

    module_point_of_sale = fields.Boolean()

    module_stock_account = fields.Boolean()

    module_barcodes = fields.Boolean()

    module_web_editor = fields.Boolean()

    module_digest = fields.Boolean()

    module_mail = fields.Boolean()

    def set_values(self):
        
        super().set_values()

        # print("\n set values --- ", self.title_in_pos)

        # print("\n self id ---- ", self.id)
