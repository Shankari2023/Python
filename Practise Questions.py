#### a = ["test@gmail.com" , "kumar@yahoo.com" , "kiran@gmail.com"]
## output 1 = ["test" , "kiran" ,"kumar"]
## output 2 = ["gmail" , "yahoo"]

a = ["test@gmail.com" , "kumar@yahoo.com" , "kiran@gmail.com"]

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


###Q.No - 2
#a = ["apple" , "apple" , "mango" , "mango" , "orange"]
# output = {"apple" : 2 , "mango" : 2 , "orange" : 1}
# unique fruit list = ["apple" , "mango", "orange"]
# duplicate fruit list ["apple" , "mango"]


a = ["apple", "apple", "mango", "mango", "orange"]
d = {}
d_keys = d.keys()
for i in a:
    if i not in d_keys:
        d[i] = a.count(i)
print(d)

first_list = []
second_list = []
for i in a:
    if i not in first_list:
        first_list.append(i)
    else:
        second_list.append(i)
print(first_list)
print(second_list)

###Q.No - 3
## file 1 : has email (duplicates)
## file 2 : has email (duplicates)
## output : common user name in both the file
#dinesh@gmail
#dinesh@yahoo


a = ["aswin@gmail.com", "aarush@gmail.com", "advay@gmail.com", "nithya@yahoo.com"]
b = ["ananya@hotmail.com", "jovan@gmail.com", "advay@hotmail.com", "aswin@yahoo.com"]

print(type(a))
print(len(a))
print(a[3])

#a.append(b)
#print(a)

a.extend(b)                 #Also use, print(a+b)
print(a)

for i in a:
    print(i)

b = [i.split('@') for i in a]
print(b)

c = [i.split('@')[0] for i in a]
print(c)

d = [i.split('@')[1] for i in a]
print(d)
print(set(d))

'''
def sort_algo(inp, num):
    if not isinstance(inp, list):
        print("inp should be of type")
    elif not isinstance(num, int):
        print("num should be of type int")
    c = sorted(inp[:num])
    d = inp[num]
    c.extend(d)
    return c

a = sort_algo([500,20, 15, 1, 1, 3])
print(a)

'''



