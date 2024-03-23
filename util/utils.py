import logging
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config import *

DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}'

engine = create_engine(DB_URI)
Base = declarative_base()
# 日志
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
# session管理上下文
Session = sessionmaker(bind=engine, autocommit=True)
session = Session()

if __name__ == '__main__':
    os.system(f'sqlacodegen {DB_URI} > models.py')
