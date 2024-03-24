# coding: utf-8

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Menu(Base):
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True)
    url = Column(String(40), comment='URL')
    name = Column(String(40))
    parent_id = Column(Integer)
    authority_id = Column(Integer, index=True)
    orders = Column(Integer, comment='排序，越高越靠前')
    icon = Column(String(100))


class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'comment': '用户表'}

    id = Column(Integer, primary_key=True, comment='主键')
    user_name = Column(String(40), comment='登录名')
    nick_name = Column(String(40), comment='显示名称')
    email = Column(String(100), comment='邮箱')
    phone = Column(String(20), comment='手机号')
    sex = Column(Integer, comment='性别 0-未知 1男 2女')
    avatar = Column(String(200), comment='头像')
    password = Column(String(40), comment='密码')
    comment = Column(String(100), comment='备注')
