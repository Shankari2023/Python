
print("Hi")

###SQL connect

from sqlalchemy import create_engine
import pandas as pd
import pymysql


###How to create engine

sqlengine = create_engine("mysql+pymysql://root:Shivamysql2023*@localhost:3306", pool_recycle=3600)

db_connect = sqlengine.connect()

df = pd.read_sql("select * from project1.emp ", db_connect)

print(df)

df['name'] = df['name'].replace(['Tommy'], 'Polo')

df.to_sql(con = db_connect, schema = "project1", name = "emp", if_exists = "replace", index = False)

import pandasql
from pandasql import sqldf

df1 = sqldf("select * from df")
print(df1)






