
# Ver : 16 

# Coded By : Vivaan Shiromani 

{
    'name': "Custom Title",

    'summary': """ Simple to use Custom title module company-wise document title change""",

    'description': """
        Simple to use Custom title module company-wise document title change
    """,

    'author': "Vivaan Shiromani",

    'category': 'Company',
    'version': '16.0.1',
    # 'price': '11.11',
    # 'currency': 'USD',

    'license': 'LGPL-3',
    
    'depends': ['base','base_setup','web'],

    'data': [
        'views/views.xml',
        'views/template.xml',
    ],

    'assets' : {

        'web.assets_backend': [

            'custom_title/static/src/js/webclient.js',

        ],
    },
    
}
