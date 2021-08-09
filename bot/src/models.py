from sqlalchemy import Column, create_engine
from sqlalchemy import Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class dbinfo():
    db_name = 'dnf'
    user_name = 'root'
    user_pwd = '123.com'
    ip = '127.0.0.1'
    port = '3306'

conn = "mysql+pymysql://{user}:{pwd}@{ip}:{port}/{db_name}?charset=utf8mb4"
connect_info = conn.format(user=dbinfo.user_name, pwd=dbinfo.user_pwd, db_name=dbinfo.db_name, ip = dbinfo.ip, port = dbinfo.port)
Base = declarative_base()
engine = create_engine(connect_info)
DBSession = sessionmaker(bind=engine)


class PICS(Base):
    __tablename__ = 'pics'


    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    path = Column(String(255))

class RAID(Base):
    __tablename__ = 'raid'

    id = Column(Integer, primary_key=True)
    wave = Column(String(255))
    team = Column(String(255))
    qq = Column(String(255))
    role = Column(String(255))



