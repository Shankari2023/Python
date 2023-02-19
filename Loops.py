#if
#while
#for

##if loop -----> decision making statement

##if else

name = "Aswin"
mark = "80"

if name == "Aswin" and mark == "80":
    print("yes")
else:
    print("no")

##nested if
name = "Aswin"
mark = 90
if name == "Aswin" and mark > 50:
    if mark > 85:
        print("Outstanding")
    else:
        print("First Class")
else:
    print("Pass")

##if - elif

name = "Aswin"
mark = 90
if mark == 100:
    print("centum")
elif mark >= 90:
    print("A Grade")
elif mark >= 60:
    print("First class")
elif mark >= 40:
    print("Third Class")
else:
    print("Fail")

### while loop ------> once condition is True, it starts executing till the condition becomes false.
### Chances of going to infinite loop if the conditional statement is not properly given
a = 1

while a<5:      #True
    print(a)
    a = a + 1

### For loop

a = list(range(10))
print(a)

a = tuple(range(10))
print(a)

a = set(range(10))
print(a)

a = list(range(10,15))
print(a)

a = list(range(10,15,2))
print(a)

for i in range(5):
    print(i)

a = [ "Hello", "Welcome", "to", "Tamilboomi"]
for i in a:
    print(i)

a = "Hello Welcome to Tamilboomi, Today we are learning Python"
a = a.split(" ")
print(a)
for i in a:
    if i == "Today":
        print(i + " has occured")

a = {"name" : "dinesh", "age" : "12", "location" : "chennai"}
for i in a.keys():
    print(i)

for i in a.values():
    print(i)

for k,v in a.items():
    print(f"key is : {k}")      #also use print("Key is", k)
    print(f"value is : {v}")    #also use print("Value is", v)

### list of all even numbers
#Step 1: Generate all numbers from 10 to 20
#Step 2:
l = []
for i in range(10,20):
    if i % 2 == 0:
        l.append(i)
        #print(l)
    #print(l)
print(l)

#### a = ["test@gmail.com" , "kumar@yahoo.com" , "kiran@gmail.com"]
## output 1 = ["test" , "kiran" ,"kumar"]
## output 2 = ["gmail" , "yahoo"]

###a = ["apple" , "apple" , "mango" , "mango" , "orange"]
# output = {"apple" : 2 , "mango" : 2 , "orange" : 1}
# unique fruit list = ["apple" , "mango", "orange"]
# duplicate fruit list ["apple" , "mango"]

