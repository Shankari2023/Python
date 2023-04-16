import dbcredentials
from db import dbfile       #from file name(class) import class name

def main():

    user_argument = getargs.get_input_args()
    print(user_argument)
    uname,pwd = dbcredentials.getdbcredentials()
    database = dbfile(uname, pwd)                   #initialised using object(database)
    engine = database.create_engine
    df = database.get_all_data(engine)
    print(df)
    print("hi")

if __name__ == "main":
    main()

