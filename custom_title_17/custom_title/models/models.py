# -*- coding: utf-8 -*-

from odoo import api, fields, Command, models, _


class custom_title(models.Model):
    _inherit = 'res.company'

    document_title = fields.Char("Document Title", store=True)


    @api.model
    def return_document_title(self):

        active_company = self.env.company.id
        
        active_company = self.env['res.company'].browse(active_company)
        
        return active_company.document_title
    
class BdPOSModuleToggle(models.TransientModel):
    _inherit = 'res.config.settings'

    module_point_of_sale = fields.Boolean()

    module_stock_account = fields.Boolean()

    module_barcodes = fields.Boolean()

    module_web_editor = fields.Boolean()

    module_digest = fields.Boolean()

    module_mail = fields.Boolean()

    def set_values(self):
        
        super().set_values()

        if self.module_point_of_sale:
        
            self.module_stock_account = True
            self.module_barcodes = True
            self.module_web_editor = True
            self.module_digest = True
            self.module_mail = True

            # current company --> title --> search for point_of_sale.index ext id 
            # then update arch_base field by modifying title 

            # if title is False then do nothing 
        
        else:
    
            self.module_point_of_sale = False
            self.module_stock_account = False
            self.module_barcodes = False
            self.module_web_editor = False
            self.module_digest = False
            self.module_mail = False




