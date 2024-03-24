from sqlalchemy.orm import defer

from util import result
from util.models import User
from util.utils import session

user_map = {
    'id': 'id',
    'user_name': 'userName',
    'nick_name': 'nickName',
    'email': 'email',
    'phone': 'phone',
    'sex': 'sex',
    'avatar': 'avatar',
    'comment': 'comment',
}


def serialized_users(users):
    serialized_user = []
    for user in users:
        user_dict = user.__dict__
        new_user = {}
        for key, value in user_map.items():
            new_user[value] = user_dict[key]
        serialized_user.append(new_user)
    return serialized_user


def save_user(user):
    user.id = None
    session.add(user)
    session.flush()
    return result.Result().success()


def del_user(user_id):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        return result.Result().success()
    else:
        return result.Result().fail()


def update_user(user):
    user_to_update = session.query(User).filter_by(id=user.id).first()
    if user_to_update:
        if user.user_name:
            user_to_update.user_name = user.user_name
        if user.nick_name:
            user_to_update.nick_name = user.nick_name
        if user.email:
            user_to_update.email = user.email
        if user.phone:
            user_to_update.phone = user.phone
        if user.sex:
            user_to_update.sex = user.sex
        if user.avatar:
            user_to_update.avatar = user.avatar
        if user.password:
            user_to_update.password = user.password
        if user.comment:
            user_to_update.comment = user.comment
        session.add(user_to_update)
        session.flush()
        return result.Result().success()
    else:
        return result.Result().fail()


def get_page(current_page, page_size, name):
    offset = (current_page - 1) * page_size
    data = (session.query(User).
            filter(User.nick_name.like('%' + name + '%'))
            .options(defer(User.password))
            .slice(offset, offset + page_size).all())
    data = serialized_users(data)
    total = session.query(User).count()
    records = {'records': data, 'total': total}
    return result.Result(data=records).success()


def user_del_batch(numbers):
    users_to_delete = session.query(User).filter(User.id.in_(numbers))
    for user in users_to_delete:
        session.delete(user)
    session.flush()
    return result.Result().success()
