# -*- coding: utf-8 -*-

# ver : 17 

{
    "name": "Custom Title",
    "summary": """Simple to use Custom title module company-wise document title change""",
    "description": """
       Simple to use Custom title module company-wise document title change
    """,
    "author": "Vivaan Shiromani",
    "category": "Company",
    "version": "1.0",
    # "price": "11.11",
    # "currency": "USD",
    "license": "LGPL-3", 
    
    "depends": ["base","base_setup","web"],
    
    "data": [
        "views/template.xml",
        "views/views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "custom_title/static/src/web/webclient/webclient.js",
        ],
    },

}
