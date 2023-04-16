#### Encapsulation
###public ----> can be used anywhere or can be modified anywhere
###protected --> _ in front ,can be used by the parent and the inherited child class
####private ---> __ in front ,can be used only within the class

### public

class test():
    name = "dinesh"
a = test()
print(a.name)
a.name = "kumar"
print(a.name)

'''
#private with error

## private

class test():
    __name = "dinesh"
a = test()
print(a.__name)
'''

#private with example

class test():
    __name = "dinesh"

    def printname(self):
        print(self.__name)
    def changename(self, a):
        self.__name = a
a = test()
a.printname()
a.changename("kumar")
a.printname()


#### Polymorphism
## method overriding
class parent():
    def name(self):
        print("parent")

class child(parent):
    def name(self):
        print("child")

a = child()
a.name()


## method overloading

class parent():

    def mul(self, a=1, b=1, c=1):
        print(a * b * c)

a = parent()
a.mul(1, 2)
a.mul(5, 4, 6)

