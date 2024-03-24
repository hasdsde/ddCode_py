from flask import request

from routes import app
from service import menuService
from util.models import Menu


@app.route("/menu", methods=['POST'])
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
    return menuService.save_menu(menu)


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
    return menuService.get_page(current_page, page_size, name, parent_id)


@app.route("/menu/parent")
def get_all_parent():
    return menuService.get_all_parent()


@app.route("/menu/child")
def get_all_child():
    return menuService.get_all_child()


@app.route("/menu/del/batch", methods=['DELETE'])
def menu_del_batch():
    data = request.get_json();
    return menuService.menu_del_batch(data)
