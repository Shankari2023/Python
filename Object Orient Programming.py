#### Classes and Objects - groups of functions doing a same logic for an object
###functions ----> group of lines doing same logic - line reduction
###classes -----> groups of functions related to particular object

'''
def truck_speed:
    print("truck speed logic")
def car_speed:
    print("car speed logic")

truck = 100 functions
car = 100 functions
200

truck fns - separate file as file 1
car fns - separate file as file
'''

###self ---> a keyword (not an argument)
##if we initialize the class - an object will be created

class truck():
    def speed(self):
        print("truck speed is 100 km/hr")
    def fuel_cap(self):
        print("fuel_cap is 50 l")

class car():
    def speed(self):
        print("car speed is 150 Km/hr")
    def fuel_cap(self):
        print("fuel_cap is 15 l")

a = truck()
print(truck)
print(a)
a.speed()
a.fuel_cap()
b = car()
b.speed()
b.fuel_cap()

a = "test"
print(a)        #in-built function

a = a.isalpha()     #in-built class
print(a)

class calc():
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
obj = calc()
a = obj.add(5,4)
print(a)

dir(obj)

obj.__class__()

class hotel():

    def floor(self,a):
        if a == 1:
            print("Veg floor")
        elif a == 2:
            print("Non-veg floor")

    def dish(self,a):
        if a == 1:
            print("Veg Briyani")
        elif a == 2:
            print("Non-veg Briyani")

a = hotel()
a.floor(2)
a.dish(2)

a = hotel()
a.floor(2)
a.dish(1)


###When argument is passed by user, there are chances of error.
###To overcome the above issue(logical error) constructor is used
####Constructor
### one time configuration for the class, variables stored in instance variable (ie , self.hotelfloor is like a cache memory

class hotel():

    def __init__(self,flr):             ##__init__   ----> constructor/initializer
        print("inside the constructor") ## just for reference it defaultly calls the constructor
        self.hotelfloor = flr

    def floor(self):
        if self.hotelfloor == 1:
            print("Veg floor")
        elif self.hotelfloor == 2:
            print("Non-veg floor")

    def dish(self):
        if self.hotelfloor == 1:
            print("Veg Briyani")
        elif self.hotelfloor == 2:
            print("Non-veg Briyani")
a = hotel(1)
a.floor()
a.dish()

b = hotel(2)
b.floor()
b.dish()

class gold():

    def bill_rate(self, todays_rate,gram):
        amount = todays_rate * gram
        print(f"Your bill amount is {amount}")

a = gold()
a.bill_rate(5000,10)

a = gold()
a.bill_rate(5500,10)

class gold():

    def __init__(self, todays_rate):
        self.todays_rate = todays_rate

    def bill_rate(self, gram):
        amount = self.todays_rate * gram
        print(f"Your bill amount is {amount}")

a = gold(5000)
a.bill_rate(20)

###Types of variables
class employee():

    emp_id = 1          ##STATIC VARIABLE ---> inside the class, outside the method

    def __init__(self, name):
        self.name = name        ### self.name ----> instance variable

    def display(self, age):     ### age ---> argument to the method
        sal = 1000              ### sal --> local variable
        print(self.emp_id)
        print(self.name)
        print(age)
        print(sal)

a = employee("dinesh")
a.display("30")

b = employee("Kumar")
b.display("45")

#####Inheritance

class calc():
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)

class calc1(calc):
    def mul(self,a,b):
        print(a*b)

a = calc1()
a.add(5,4)
a.sub(5,4)
a.mul(5,4)

#### Simple Inheritance - 1 parent 1 child
###simple inheritance using Constructor in child class
class parent():

    def demo(self):
        print("demo")

class child(parent):

    def __init__(self):
        self.money = 1000

    def display(self):
        print(self.money)

a = child()
a.display()

###single inheritance using Constructor in both in parent and in child
class parent():

    def __init__(self):
        self.name = "dinesh"

    def demo(self):
        print("demo")

class child(parent):

    def __init__(self):
        self.money = 1000
        super().__init__()

#keyword super() ----> to keep the parental class constructor(one-time memory) value in memory

    def display(self):
        print(self.money)
        print(self.name)

a = child()
a.display()

###Multi-level Inheritance
class calc():

    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)

class calc1(calc):
    def mul(self,a,b):
        print(a*b)

class calc2(calc1):
    def div(self,a,b):
        print(a/b)

a = calc2()
a.add(5,4)
a.sub(5,4)
a.mul(5,4)
a.div(5,4)

### Multi-level inheritance
class parent():

    def __init__(self):
        self.name = "dinesh"

    def demo(self):
        print("demo")

class child(parent):

    def __init__(self):
        self.money = 1000
        super().__init__()

class grandchild(child):
    def __init__(self):
        self.age = "12"
        super().__init__()

    def display(self):
        print(self.money)
        print(self.name)
        print(self.age)

a = grandchild()
a.display()

###Hierarchial Inheritance

class parent():

    def name(self):
        print("parent")

class child(parent):
    def child(self):
        print("child")

class grandchild(child):
    def grandchild(self):
        print("grandchild")

a = child()
a.name()
a.child()

b = grandchild()
b.name()
b.grandchild()

#### Multiple Inheritance
class parent():

    def name(self):
        print("parent")

class child():
    def child(self):
        print("child")

class grandchild(parent, child):
    def grandchild(self):
        print("grandchild")

a = grandchild()
a.name()
a.child()
a.grandchild()

class parent():

    def __init__(self):
        self.parent = "parent"

class child():

    def __init__(self):
        self.child = "child"

class grandchild(parent, child):
    def __init__(self):
        self.grandchild = "grandchild"
        super().__init__()
        super(parent,self).__init__()


    def display(self):
        print(self.parent)
        print(self.child)
        print(self.grandchild)

a = grandchild()
a.display()


####Abstraction
from abc import ABC, abstractmethod  ###abc ---> abstract class

class parent(ABC):

    @abstractmethod
    def bat(self):
        pass

    @abstractmethod
    def ball(self):
        pass

class play(parent):
    def bat(self):
        print("bat")
    def ball(self):
        print("ball")
    def stump(self):
        print("stump")
    def glove(self):
        print("glove")

a = play()
