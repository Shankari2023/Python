#arrays of data
### filter, map, reduce -------> it takes 2 arguments
#first function name    #second, input to the function
# filter ----> only returns true value
# map -------> returns the value True or false
# reduce ---->


#### filter ----> only returns true value
def even(n):
    print("function has started")
    if n%2 == 0:
        return True
    else:
        return False
a = [1,2,3,4,5,6,7,8,9,10]
b = filter(even,a)
print(list(b))

a = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x:x%2==0,a)))      #lambda - inline function

##### map --------> it returns the values as True or False
def even(n):
    print("function has started")
    if n%2 == 0:
        return True
    else:
        return False
a = [1,2,3,4,5,6,7,8,9,10]
b = map(even,a)
print(list(b))

a = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x:x%2==0,a)))

#### reduce  ----------> import

from functools import reduce
def sum(m,n):
    return m + n
a = [1,2,3,4,5,6,7,8,9,10]
print(reduce(sum,a))

a = [1,2,3,4,5,6,7,8,9,10]
print(reduce(lambda n,m : n+m,a))

###list comprehension

a = [x for x in range(10)]
print(a)

l = []
for i in range(10):
    l.append(i)
print(l)

a = [x for x in range(10,100) if x%2 == 1]
print(a)

l = []
for i in range(10,100):
    if i%2 == 1:
        l.append(i)
print(l)

####bool -------> to find out any values are given in the list/tuple/set/dictionary
a = []
if bool(a):
    print("Value is there")
else:
    print("No values")


#### if ..... in
a = ("test", "demo", "hello")
if "hi" not in a:
    print("yes")

####dict comprehension
a = {x : x**2 for x in range(5)}
print(a)

a = ["one", "two", "three"]
b = [1,2,3]
c = zip(a,b)            #to join the two list of equal length
print(dict(c))

##### random
import random
a = [22, 33, 44, 21, 23, 43, 23, 54]
print(random.choice(a))         # -----> randomly chooses any values of a

print(random.sample(a,4))       # -----> randomly chooses any 4 values of a

random.shuffle(a)               # -----> randomly shuffles a(the given list)
print(a)

print(random.random())             #------>random decimal between 0 - 1

print(random.randrange(0,500))   #---->used for otp generations

print(random.uniform(1,5))   #------>random decimal between 1 to 5


import string
import random
print(random.choice(string.ascii_letters))  #generates string for otp (eg password generation)
print(random.randint(0,9))                  #generates number randomly


"".join(random.choice(string.ascii_letters) for i in range(10))

"".join(random.choice(string.punctuation)for i in range(3))

"".join(random.choice(string.digits)for i in range(3))

pwd = "".join(random.choice(string.ascii_letters) for i in range(10)) + \
      "".join(random.choice(string.punctuation)for i in range(3)) + \
    "".join(random.choice(string.digits)for i in range(3))
print(pwd)
pwd = (list(pwd))
random.shuffle(pwd)
print("".join(pwd))

#####Math
import math
print(math.ceil(22.09))     #ceil -----> rounds to maximum value
print(math.ceil(-22.09))
print(math.ceil(22))

print(math.floor(22.09))    #floor ----> rounds to minimum value
print(math.floor(-22.09))
print(math.floor(22))

print(round(22.09))         #round -----> general round off
print(round(22.54))

####xxxxxxxxxxxxxxx
## assignment for 26 Feb 2023

## file 1 : has email (duplicates)
## file 2 : has email (duplicates)
## output : comon user name in both the file
#dinesh@gmail
#dinesh@yahoo