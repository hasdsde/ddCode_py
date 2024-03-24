from flask import request

from routes import app
from service import menu_service
from util.models import Menu


# 新增、修改
@app.route("/menu", methods=['POST', 'PUT'])
def save_menu():
    data = request.get_json()
    menu = Menu()
    menu.id = data['id']
    menu.url = data['url']
    menu.name = data['name']
    menu.parent_id = data['parentId']
    menu.authority_id = data['authorityId']
    menu.orders = data['orders']
    menu.icon = data['icon']
    if menu.id:
        return menu_service.update_menu(menu)
    else:
        return menu_service.save_menu(menu)


# 分页查询
@app.route('/menu/page')
def get_page():
    current_page = request.args.get('currentPage', 1)
    name = request.args.get('name')
    parent_id = request.args.get('parentId', None)
    page_size = request.args.get('pageSize', 15)
    if parent_id:
        parent_id = int(parent_id)
    current_page = int(current_page)
    page_size = int(page_size)
    return menu_service.get_page(current_page, page_size, name, parent_id)


# 查询父级
@app.route("/menu/parent")
def get_all_parent():
    return menu_service.get_all_parent()


# 查询子级
@app.route("/menu/child")
def get_all_child():
    return menu_service.get_all_child()


# 删除
@app.route("/menu/del/batch", methods=['DELETE'])
def menu_del_batch():
    data = request.get_json();
    return menu_service.menu_del_batch(data)
