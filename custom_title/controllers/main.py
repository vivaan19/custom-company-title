from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.home import Home
from odoo.addons.point_of_sale.controllers.main import PosController
from bs4 import BeautifulSoup


class FetchCurrentCompanyDocTitle(http.Controller):

    # controller called everytime when page gets refreshed 

    @http.route("/current_company_doc_title", auth="user", type="json")
    def FetchDocTitle(self, **kwargs):
    
        try:
            company = request.env['res.company'].browse(kwargs.get('comp_id'))

            # print("\n company --- ", company)
            
            if not company.exists():
                return {"current_company_title": "Odoo"}
            
            document_title = company.document_title

            # print("\n Document title pre ---- ", document_title)

            if not document_title:
                document_title = "Odoo"

            # for pos arch base update ---- 
            ir_view_rec = request.env["ir.ui.view"].sudo().search([("name", "ilike", "POS Index")], limit=1)

            if ir_view_rec:
                
                # POS is installed 
                
                # First setup the setting inside arch_base
                # Inject Custom title settings in config settings in POS 

                view_name = "res.config.settings.view.form.inherit.point_of_sale"
                ir_view_rec_pos = request.env["ir.ui.view"].sudo().search([("name", "ilike", view_name)], limit=1)

                # print("\n Pos setting view ---- ", ir_view_rec_pos)

                soup_pos_setting = BeautifulSoup(ir_view_rec_pos.arch_base, 'html.parser')

                h2_custom_tite_tag = soup_pos_setting.find('h2', string='Custom Title in POS')

                if h2_custom_tite_tag:
                    pass
                
                else:
                    h2_accounting_tag = soup_pos_setting.find('h2', string='Accounting')

                    # print("\n In else ---- accounting tag ", h2_accounting_tag)
                    
                    new_html_content = ''' 
                        <div id="custom_title_in_pos">

                            <h2>Custom Title in POS</h2>

                            <div class="row mt16 o_settings_container" name="custom_title_toggle">

                                <div id="custom_title_toggle" class="col-12 col-lg-6 o_setting_box"
                                    help="Provide Custom Title in POS"
                                    title="Provide Custom Title in POS">

                                    <div class="o_setting_left_pane">
                                        <field name="title_in_pos" string="Enable Custom Title in POS"/>
                                    </div>

                                    <div class="o_setting_right_pane">
                                        <label for="title_in_pos"/>
                                    
                                    <div class="text-muted">
                                        Helps to Enable Custom Title in POS
                                    </div>
                                
                                </div>
                                
                                </div>
                            
                            </div>
                        </div>
                    '''

                    new_content_soup = BeautifulSoup(new_html_content, 'html.parser')
                    
                    h2_accounting_tag.insert_before(new_content_soup)

                    added_custom_title_setting = str(soup_pos_setting)

                    ir_view_rec_pos.sudo().write({
                        "arch_base": added_custom_title_setting,
                        "arch_db": added_custom_title_setting
                    })

                # print("\n res setting ---- ", request.env["res.config.settings"].sudo().search([]))

                latest_res_config_id = request.env["res.config.settings"].sudo().search([]).mapped("id")[-1]

                # print("\n latest res config id --- ", latest_res_config_id)

                title_in_pos = request.env["res.config.settings"].sudo().search([("id", "=", latest_res_config_id)]).title_in_pos

                # print("\n latest title in pos ---- ", title_in_pos)

                if title_in_pos:
                
                    soup = BeautifulSoup(ir_view_rec.arch_base, 'html.parser')

                    title_tag = soup.find("title")

                    # Modify the content
                    if title_tag:
                        title_tag.string = document_title + " POS"

                    # Get the modified HTML string
                    modified_html = str(soup)

                    ir_view_rec.sudo().write({
                        "arch_base": modified_html,
                        "arch_db": modified_html,
                    })
                
                else:

                    soup = BeautifulSoup(ir_view_rec.arch_base, 'html.parser')

                    title_tag = soup.find("title")

                    # Modify the content
                    if title_tag:
                        title_tag.string = "Odoo" + " POS"

                    # Get the modified HTML string
                    modified_html = str(soup)

                    ir_view_rec.sudo().write({
                        "arch_base": modified_html,
                        "arch_db": modified_html,
                    })

            # print("\n Document title ---- ", document_title)
            
            return {"current_company_title": document_title}
        
        except Exception as e:

            # print("Exception ---- ", e)
            
            return {"current_company_title": "Odoo"}


# controller for title persistant after log-out 
class CustomHome(Home):

    @http.route('/web/login', type='http', auth="none")
    def web_login(self, redirect=None, **kw):
        
        response = super(CustomHome, self).web_login(redirect=redirect, **kw)
        
        # when log-out is called 
        if request.httprequest.method == 'GET' and isinstance(response, http.Response):

            custom_title = "Odoo" 
            
            try: 

                cookie_cids = request.httprequest.cookies.get('cids')

                if cookie_cids:

                    query = """
                        SELECT document_title
                        FROM res_company
                        WHERE id = %s
                    """

                    request.env.cr.execute(query, (cookie_cids,))
                    
                    result = request.env.cr.fetchone()

                    custom_title = result[0]

                    # # print("\n result ----- ", result[0])
                    
                    # custom_title = request.env["res.company"].sudo().search([("id", "=", cookie_cids)]).document_title

                    # # print("\n custom ttile --- ", custom_title)

                    if not custom_title:
                        custom_title = "Odoo"
            
            except Exception as e:

                # # print("\n e ---- ", e)
                
                custom_title = request.env["res.company"].search([], limit=1).document_title
                
                if not custom_title:
                    custom_title = "Odoo"

            # print("\n custom title in login ---- ", custom_title)            
            
            response.qcontext.update({'custom_title': custom_title})

        return response


# class BDPosController(PosController):

#     @http.route(['/pos/web', '/pos/ui'], type='http', auth='user')
#     def pos_web(self, config_id=False, **k):
        
#         response = super(BDPosController, self).pos_web(config_id=False, **k)

#         # when log-out is called 

#         custom_title = "Odoo POS"
        
#         try: 

#             cookie_cids = request.httprequest.cookies.get('cids')

#             if cookie_cids:
                
#                 custom_title = request.env["res.company"].search([("id", "=", int(cookie_cids))]).document_title
                

#                 if not custom_title:
#                     custom_title = "Odoo POS"
#                 else:
#                     custom_title = str(custom_title) + " POS"

        
#         except Exception as e:
            
#             custom_title = request.env["res.company"].search([], limit=1).document_title
            
#             if not custom_title:
#                 custom_title = "Odoo POS"
            
#             else:
#                 custom_title = str(custom_title) + " POS"

                        
#         response.qcontext.update({'custom_title': custom_title})

#         return response



