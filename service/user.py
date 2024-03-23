from util.models import User
from util.utils import session


def add_user(user):
    session.add(user)
    session.commit()


def check(name, password):
    res = session.query(User).filter(User.name == name, User.password == password).first()
    session.commit()
    print(res)
    if res:
        return True
    else:
        return False
