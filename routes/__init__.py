from flasgger import Swagger, swag_from
from flask import *

app = Flask(__name__, template_folder='../template', static_folder="../static")
swagger = Swagger(app)

specs_dict = {
    "definitions": {
        "Menu对象": {
            "type": "object",
            "properties": {
                "authorityId": {
                    "type": "integer",
                    "format": "int32",
                    "description": "权限Id"
                },
                "icon": {
                    "type": "string",
                    "description": "图表"
                },
                "id": {
                    "type": "integer",
                    "format": "int32",
                    "description": "主键"
                },
                "name": {
                    "type": "string",
                    "description": "名称"
                },
                "orders": {
                    "type": "integer",
                    "format": "int32",
                    "description": "排序，越高越靠前"
                },
                "parentId": {
                    "type": "integer",
                    "format": "int32",
                    "description": "父级Id"
                },
                "url": {
                    "type": "string",
                    "description": "URL"
                }
            },
            "title": "Menu对象",
            "description": "menu"
        },
        "User对象": {
            "type": "object",
            "properties": {
                "avatar": {
                    "type": "string",
                    "description": "头像"
                },
                "comment": {
                    "type": "string",
                    "description": "备注"
                },
                "email": {
                    "type": "string",
                    "description": "邮箱"
                },
                "id": {
                    "type": "integer",
                    "format": "int32",
                    "description": "主键"
                },
                "nickName": {
                    "type": "string",
                    "description": "显示名称"
                },
                "password": {
                    "type": "string",
                    "description": "密码"
                },
                "phone": {
                    "type": "string",
                    "description": "手机号"
                },
                "sex": {
                    "type": "integer",
                    "format": "int32",
                    "description": "性别 0-未知 1男 2女"
                },
                "userName": {
                    "type": "string",
                    "description": "登录名"
                }
            },
            "title": "User对象",
            "description": "用户表"
        }
    }
}


@swag_from(specs_dict)
@app.route("/")
def root():
    return redirect("http://localhost:9000/")


from routes import menu_route, user_route
