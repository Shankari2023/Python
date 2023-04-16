

def getdbcredentials():


    file_details = open("credentials.txt", "r")
    for i in file_details:
        if "username" in i:
                user_name = i.split("=")[1].strip()
        elif "password" in i:
                user_pwd = i.split("=")[1].strip()
    return user_name, user_pwd
