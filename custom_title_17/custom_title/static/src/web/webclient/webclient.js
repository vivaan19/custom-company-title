/** @odoo-module **/

import { WebClient } from "@web/webclient/webclient";
import { patch } from "@web/core/utils/patch";
import { session } from "@web/session";
import { jsonrpc } from "@web/core/network/rpc_service";

import { cookie } from "@web/core/browser/cookie";


patch(WebClient.prototype, {
    /**
     * @override
    */
    setup() {

        super.setup();
        this.getCustomTitle();

    },

    async getCustomTitle() {

        try {

            if (!cookie || !cookie.get("cids")) {
                return;
            }

            try {

                var comp_id = cookie.get("cids");

                console.log("Session current company ----- ", session);

            }

            catch {

                return;
            }

            const company_data = {
                "comp_id": comp_id,
            }

            console.log("Company Data === ", company_data);

            // ajax.jsonRpc does not require seperate Qunit test-case 
            const result = await jsonrpc('/current_company_doc_title', company_data);

            console.log("Result ---- ", result);

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
            return;
        }

    }
});

