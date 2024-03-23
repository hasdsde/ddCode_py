from util.models import User
from util.utils import session

user = session.query(User).where(User.user_name == 'admin').first()
user.nick_name = "adminssss"
session.commit()
session.close()
