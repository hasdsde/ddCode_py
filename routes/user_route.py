from flask import request

from routes import app
from service import user_service
from util.models import User


# 新增 修改
@app.route("/user", methods=['POST', 'PUT'])
def save_user():
    data = request.get_json()
    user = User()
    user.id = data['id']
    user.user_name = data['userName']
    user.nick_name = data['nickName']
    user.email = data['email']
    user.phone = data['phone']
    user.sex = data['sex']
    user.avatar = data['avatar']
    user.password = data['password']
    user.comment = data['comment']
    if user.id:
        return user_service.update_user(user)
    else:
        return user_service.save_user(user)


# 分页查询
@app.route('/user/page')
def get_user_page():
    current_page = request.args.get('currentPage', 1)
    nick_name = request.args.get('nickName')
    page_size = request.args.get('pageSize', 15)
    current_page = int(current_page)
    page_size = int(page_size)
    return user_service.get_page(current_page, page_size, nick_name)


# 删除
@app.route("/user/batch", methods=['DELETE'])
def user_del_batch():
    data = request.get_json()
    return user_service.del_user(data)
