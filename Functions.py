#functions - Function oriented programming language

#Add 2 numbers - using functions    ---------> user-defined function
def add(a,b):               #def -----> define a function
    print(a+b)              #add -----> function name
add(5,4)                    # a, b ---> argument name


def add(a,b):
    return(a+b)
a = add(5,4)
print(a)
b = add(a,10)
print(b)

def add(a,b):
    c = a+b
    print(f"start of function {c}")
    return c
    print("after return")
add(5,4)

#Types of variable
# local variable
# global variable

a = "welcome"           #global variable
def test():
    a = "hello"         #local variable
test()
print(a)

a = "welcome"
def test():
    a = "hello"
    return a
print(a)
a = test()
print(a)

a = "welcome"
def test():
    a = "hello"
    print(a)
print(a)
test()
print(a)

a = "welcome"
def test():

    a = "hello"
    print(a)
test()
print(a)
print(a)

a = "welcome"
def test():
    global a
    a = "hello"
    print(a)
test()
print(a)
print(a)

#Ways of passing arguments/Argument Handling

def add(a,b):
    return(a+b)
a = add(10,20)
print(a)
b = add(a,25)
print(b)

def add(a,b,c):
    return(a+b+c)
a = add(5,3,7)
print(a)
b = add(a,10,1)
print(b)
c = add(b,6,4)
print(c)


#Positional arguments
def name(f_name, m_name, l_name):
    print("first name is ", f_name)
    print("middle name is ", m_name)
    print("last name is ", l_name)
name("Sachin", "Ramesh", "Tendulkar")

#keyword arguments
name(l_name = "sachin", f_name="Ramesh", m_name="Tendulkar")

#default argument
def name(f_name = None, m_name = None, l_name = None):
    print("first name is ", f_name)
    print("middle name is ", m_name)
    print("last name is ", l_name)
name("Sachin")

#positional argument follows keyword argument
#non default argument follows default argument
def name(f_name = None,m_name = None,l_name = None):
    print("first name is ", f_name)
    print("middle name is ", m_name)
    print("last name is ", l_name)
#name(l_name = "sachin", f_name="Ramesn", "Tendulkar") #shows error because m_name is not given

def test(*args):
    print(args)
    a=args[0]
    b=args[1]
    print(a,b)
test("hello",1,3,4,5,"welcome")


def test(**kwargs):
    print(kwargs)
    name=kwargs.get("name")
    state=kwargs.get("state")
    print(name,state)
    return name,state
test(name="test", add1="add1", add2="add2", state="state")

def test(a, *b):
    print(a)
    print(b)            #other than first position
test(1)
test(1,2,3,4,5)

def mul(a,b,c=1):           #1 is null value to arithmetic variable
    print(a*b*c)
mul(3,4)

###lambda -----> inline function (to write 3-4 step codes in one line)

a = lambda a,b: a+b
a(5,4)

