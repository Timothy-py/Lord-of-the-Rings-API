template = {
    # "openapi": "3.0",
    "swagger": "2.0",
    "info": {
        "title": "Lord of the Rings Characters API",
        "description": "API for Characters and Quotes from Lord of the Rings Movie",
        "contact": {
            "responsibleDeveloper": "DScipher:Timothy",
            "email": "adeyeyetimothy33@gmail.com",
            "url": "https://www.timothyadeyeye.netlify.app",
        },
        "version": "1.0"
    },
    "basePath": "/api/v1",  # base bash for blueprint registration
    "schemes": [
        "http",
        "https"
    ],
    "securityDefinitions": {
        "Authorization": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "JWT Authorization header using the Bearer scheme. Example: \"Authorization: Bearer {token}\""
        }
        # "Authorization": {
        #     "type": "http",
        #     "scheme": "bearer",
        #     "bearerFormat": "JWT",
        #     "description": "JWT Authorization header using the Bearer scheme. Example: \"Authorization: Bearer {token}\""
        # }
    },
}

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/"
}
