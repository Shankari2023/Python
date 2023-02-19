
a = "Welcome to today's class"
# a is a variable
## value - data
# data types

#str something comes in quotes
a = "test"
print(type(a))
print(isinstance(a,str))

a = "SachinTendulkar"
#Based on ASCII values alphabets gets sorted
print(len(a))   #Length
print(min(a))   #minimum value
print(max(a))   #maximum value
print(sorted(a))    #sorts in ascending order

print(a.isalpha())  #checks the string is alphabetic or not
print(a.isalnum())  #checks the string is alphabet or numeric
print(a.isdigit())  #checks the string has numbers
print(a.isupper())  # upper case or not
print(a.islower())  # lower case or not
print(a.upper())    # changes all the words to upper case
print(a.lower())    # changes all the words to lower case
print(a.swapcase())

a = "welcome to today's class"
print(a.title())
print(a.capitalize())

# FORWARD INDEXING
# ---------------------->
# 0  1  2  3  4  5
# P  Y  T  H  O  N
#-6 -5 -4 -3 -2 -1
# <---------------------

a = "SachinTendulkar"
print(a[5])

#start:stop:interval

print(a[2:10])
print(a[:])
print(a[-1])
print(a[::1])
print(a[::2])
print(a[::3])

print(a[::-1])

print(a[-14:-1:-1])

print(a.index("n"))
print(a.index("a"))
print(a.index("a",2))
print(a.index("a",2,14))
print(a.index("z"))

print(a.rindex("n"))
print(a.rindex("a"))
print(a.rindex("z"))

#print(a.index("a",start,end)

#find and rfind
#find and index is the same - unless find returns -1 if the substring is not found

a = "SachinTendulkar"
print(a.index("n"))
print(a.find("n"))
print(a.find("z"))

print(a.rindex("n"))
print(a.rfind("n"))
print(a.rfind("z"))

print(a.count("a"))             #counts a word
print(a.replace("a", "$"))      #find and replace
print(a.replace("a", "$", 1))   #find and replace first occurance
print(a.replace("a", "$", 2))   #find and replace two occurance
print(a.split("a"))             #split the occurance
print(a.split("a", 1))          #split based on the first occurance

print(a.startswith("S"))
print(a.endswith("r"))

print("Good Morning {}, Have a Great {}".format("Shiva", "Sunday"))
print("Good Morning {1}, Have a Great {0}".format("Shiva", "Sunday"))

name = "Shiva"
day = "Sunday"
#print{f"Good Morning {name} , Have a Great {day}"}

print("Good Morning {Shiva}, Have a Great {Sunday}")

a = 123
print(type(a))
print(isinstance(a,str))

a = "123"
print(type(a))
print(isinstance(a,int))
print(isinstance(a,str))
print(a.isdigit())

a = "123"
print(a.isdigit())


a = 123.45
print(type(a))

a = "123"
print(int(a))
print(float(a))

a = input("Enter your name: ")
print(a)
