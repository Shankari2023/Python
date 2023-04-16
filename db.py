from sqlalchemy import create_engine
import pandas as pd
import pymysql
from dbabstract import dbabstract

class dbfile(dbabstract):

    DB_NAME = "project1"
    TBL_NAME = "emp"

    def __init__(self, uname, pwd):     #initialise uname and pwd using this constructor
        self.__username = uname         #uname and pwd as private variable
        self.__pwd = pwd

    def create_engine(self):            #creating database connection and returning it
        db_path = "mysql+pymysql://{}:{}@localhost:3306".format(self.__username, self.__pwd)
        sqlengine = create_engine(db_path, pool_recycle = 3600)
        engine = sqlengine.connect()
        return engine

    def get_all_data(self, engine):
        sql = "select * from {}.{}".format(self.DB_NAME, self.TBL_NAME)
        df = pd.read_sql(sql, engine)
        return df




