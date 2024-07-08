from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.home import Home
from odoo.addons.point_of_sale.controllers.main import PosController

from bs4 import BeautifulSoup


class FetchCurrentCompanyDocTitle(http.Controller):

    @http.route("/current_company_doc_title", type="json", auth="user")
    def FetchDocTitle(self, comp_id):

        print("\n in controller ---- ", comp_id)
    
        try:
            company = request.env['res.company'].sudo().search([("id", "=", comp_id)])
            
            document_title = company.document_title

            # for pos arch base update ---- 
            if not document_title:
                pass
            
            else:
                
                ir_view_rec = request.env["ir.ui.view"].sudo().search([("name", "ilike", "POS Index")], limit=1)

                if not ir_view_rec:
                    pass
                
                else:
                    soup = BeautifulSoup(ir_view_rec.arch_base, 'html.parser')

                    title_tag = soup.find("title")

                    # Modify the content
                    if title_tag:
                        title_tag.string = document_title + " POS"

                    # Get the modified HTML string
                    modified_html = str(soup)

                    ir_view_rec.sudo().write({
                        "arch_base": modified_html,
                    })

            return {"current_company_title": document_title}
        
        except Exception as e:
            
            print("\n execption ---- ", e)

            return {"current_company_title": "Odoo"}
              
class CustomHome(Home):

    @http.route()
    def web_login(self, *args, **kw):
        
        response = super(CustomHome, self).web_login(*args, **kw)

        # when log-out is called 
        if request.httprequest.method == 'GET' and isinstance(response, http.Response):

            print("\n In iff ---- ")

            custom_title = "Odoo"
            
            try: 

                cookie_cids = request.httprequest.cookies.get('cids')

                print("\n cookie cids ---- ", cookie_cids)

                if cookie_cids:

                    query = """
                        SELECT document_title
                        FROM res_company
                        WHERE id = %s
                    """

                    request.env.cr.execute(query, (cookie_cids,))
                    
                    result = request.env.cr.fetchone()

                    if result:
                        custom_title = result[0]
                    else:
                        custom_title = "Odoo"

                    # print("\n result ----- ", result[0])
                    
                    # custom_title = request.env["res.company"].sudo().search([("id", "=", cookie_cids)]).document_title

                    # print("\n custom ttile --- ", custom_title)

                    if not custom_title:
                        custom_title = "Odoo"
            
            except Exception as e:
                
                custom_title = request.env["res.company"].search([], limit=1).document_title
                
                if not custom_title:
                    custom_title = "Odoo"

            print("\n custom title in login ---- ", custom_title)    
            
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
