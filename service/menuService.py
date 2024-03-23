from util import result
from util.models import Menu
from util.utils import session

menu_map = {
    'id': 'id',
    'name': 'name',
    'url': 'url',
    'parent_id': 'parentId',
    'authority_id': 'authorityId',
    'orders': 'orders',
    'icon': 'icon',
}


def serialized_menus(menus):
    serialized_menu = []
    for menu in menus:
        menu_dict = menu.__dict__
        new_menu = {}
        for key, value in menu_map.items():
            new_menu[value] = menu_dict[key]
        serialized_menu.append(new_menu)
    return serialized_menu


def save_menu(menu):
    menu.id = None
    session.add(menu)
    session.flush()
    return result.Result().success()


def del_menu(menu_id):
    user = session.query(Menu).filter(Menu.id == menu_id).first()
    if user:
        session.delete(user)
        return result.Result().success()
    else:
        return result.Result().fail()


def update_menu(menu):
    menu_to_update = session.query(Menu).filter_by(id=menu.id).first()
    if menu_to_update:
        menu_to_update.url = menu.url
        menu_to_update.name = menu.name
        menu_to_update.parent_id = menu.parent_id
        menu_to_update.orders = menu.orders
        menu_to_update.icon = menu.icon
        return result.Result().success()
    else:
        return result.Result().fail()


def get_all_parent():
    menus = session.query(Menu).filter(Menu.parent_id.is_(None)).all()
    serialized_menu = serialized_menus(menus)
    return result.Result(data=serialized_menu).success()


def get_all_child():
    menus = session.query(Menu).filter(Menu.parent_id.isnot(None)).all()
    serialized_menu = serialized_menus(menus)
    return result.Result(data=serialized_menu).success()


def get_page(current_page, page_size, name, parent_id):
    offset = (current_page - 1) * page_size
    if parent_id:
        data = (session.query(Menu).
                order_by(Menu.orders).
                filter(Menu.name.like('%' + name + '%').__and__(Menu.parent_id.__eq__(parent_id)))
                .slice(offset, offset + page_size).all())
    else:
        data = (session.query(Menu).
                order_by(Menu.orders).
                filter(Menu.name.like('%' + name + '%'))
                .slice(offset, offset + page_size).all())
    data = serialized_menus(data)
    total = session.query(Menu).count()
    records = {'records': data, 'total': total}
    return result.Result(data=records).success()
