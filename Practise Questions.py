#### a = ["test@gmail.com" , "kumar@yahoo.com" , "kiran@gmail.com"]
## output 1 = ["test" , "kiran" ,"kumar"]
## output 2 = ["gmail" , "yahoo"]


a = {"name1" : "test", "name2" : "kumar", "name3" : "kiran"}
a_str = []
for i in a.values():
    a_str.append(str(i))
print(a_str)

b = {"email1" : "gmail", "email2" : "yahoo"}
b_str = []
for i in b.values():
    b_str.append(str(i))
print(b_str)



###a = ["apple" , "apple" , "mango" , "mango" , "orange"]
# output = {"apple" : 2 , "mango" : 2 , "orange" : 1}
# unique fruit list = ["apple" , "mango", "orange"]
# duplicate fruit list ["apple" , "mango"]


a = ["apple", "apple", "mango", "mango", "orange"]
b = ["2", "2", "1"]

print(type(a))
print(isinstance(a,list))
print(list(a))
print(set(a))
print(list(set(a)))



