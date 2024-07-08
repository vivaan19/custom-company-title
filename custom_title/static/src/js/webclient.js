/** @odoo-module **/

import { WebClient } from "@web/webclient/webclient";
import { patch } from "web.utils";
import { useService } from "@web/core/utils/hooks";

import session from 'web.session';
import ajax from 'web.ajax';

patch(WebClient.prototype, "custom_title.WebClient", {
    setup() {
        
        this._super();    
        this.getCustomTitle();
        
    },
    
    async getCustomTitle() {
        
        try {

            if (!session || !session.user_context || !session.user_context.allowed_company_ids) {
                return;
            }

            try {

                var comp_id = session.user_context.allowed_company_ids[0];
            }

            catch {

                return;
            }

            const company_data = {

                "comp_id": comp_id,

            }

            // ajax.jsonRpc does not require seperate Qunit test-case 
            
            var result = await ajax.jsonRpc("/current_company_doc_title", "call", company_data);

            if (result && result.current_company_title) {

                if (!result.current_company_title) {

                    this.title.setParts({ zopenerp: "Odoo" });
                }

                else {

                    this.title.setParts({ zopenerp: result.current_company_title });
                }

            }

        } catch (error) {

            this.title.setParts({ zopenerp: "Odoo" });

            console.error("Error fetching custom title:", error);

            return;
        }

    }
});

