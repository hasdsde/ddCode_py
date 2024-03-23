from flask import jsonify


class Result:
    def __init__(self, code=200, msg="", data=""):
        self.code = code
        self.response = {
            "code": code,
            "msg": msg,
            "data": data
        }

    def success(self):
        self.response['msg'] = "操作成功"
        return jsonify(self.response), self.response['code']

    def fail(self):
        self.response['msg'] = "操作失败"
        self.response['code'] = 500
        return jsonify(self.response), self.response['code']
