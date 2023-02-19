'''
a = ["Kiran", "25", "chennai"]
print(type(a))
print(isinstance(a,list))
print(len(a))
print(min(a))
print(max(a))
print(sorted(a))
print(a[0])
print(a[::-1])

a = [100, 5, 60, 54]
print(sorted(a))

a= "SachinTendulkar"
print(sorted(a))

a = [100, 5, 60, 54]
a.append(2000)          #default add at the ends
print(a)
a.insert(2, 5000)       ##adds at particular index
print(a)
a.remove(60)            #removes particular value
print(a)
del a[1]                #removes based on index
print(a)
b = a.pop()
print(a)
print(b)

a = [1,2,3]
b = [4,5,6]
a.append(b)         #adds a new list
print(a)

a = [1,2,3]
b = [4,5,6]
a.extend(b)         #to add to the existing list
print(a)            #also use print(a+b)

#copy in python
##shallow copy -------> s --- shared memory
##deep copy ---------> d --- different memory

a = [1,2,3]             ### shallow copy
b = a
a.append(4)
print(a)
print(b)

a = [1,2,3]             ### deep copy
b = a.copy()
a.append(4)
print(a)
print(b)

a = [1,2,3,4,5]
a.reverse()
print(a)


a = [1,2,3,4,5]
a[0:3]
print(a[0:3])

a.index(3)
print(a.index(3))

a = [["Kiran", "25", "chennai"], ["kumar", "28", "madurai"]]
print(a[0][2])
print(a[1][1])

a = (1,2,3)
print(type(a))
print(isinstance(a,tuple))

print(min(a))
print(a[0])
print(len(a))

'''

'''
b = a
b = a.copy()        #shows attribute error
#shallow copy able to do in tuple: but we cannot deep copy in tuple

a.append(4)         #shows attribute error
'''

'''


### bracket
### list mutable,  tuple immutable
### tuple - faster


#SET --------> no duplicates allowed (advantage)
# indexing not supported in set

a = {1,2,3}
print(type(a))

print(isinstance(a,set))

a = {1,1,1,1,2,2,2,3,3,3,3,3}
print(a)

a = ["test", "test", "try", "hello", "hello"]
print(set(a))
print(list(set(a)))
print(tuple(set(a)))

a = {50, 20, 10, 5, 6, 200}
print(len(a))
print(min(a))
print(max(a))
print(sorted(a))

print(a[10])            # indexing not supported in set


a = {1,2,3}
a.add(5)
print(a)
a.remove(3)             #removes the value only
print(a)
#pop removes the value and assigns to a new value
b = a.pop()             #in set pop removes the 1st element
print(b)
print(a)


a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a.union(b))       #removes all duplicates and join both sets together
print(a | b)
print(a.intersection(b))    #takes the common elements of both the sets
print(a & b)
print(a.difference(b))  #elements in a but not in b
print(a-b)
print(b.difference(a))  #elements in b but not in a
print(b-a)
print(a.symmetric_difference(b))    #removes the common elements
print(a^b)




a = {1,2,3,4,5}
b = {3,4}
print(a.issuperset(b))
print(b.issuperset(a))
print(a.issubset(b))
print(b.issubset(a))

'''

#Dictionary Operator loop
'''
a = (["Kiran", "20", "Chennai"], ["Madurai", "Kumar", "45"])
a = {"name" : "Kiran", "location" : "Chennai", "age" : "20"}

print(type(a))
print(isinstance(a,dict))

a = (["Kiran", "20", "Chennai"], ["Madurai", "Kumar", "45"])
print(a[0][2])

a = {"name" : "Kiran", "location" : "Chennai", "age" : "20"}

print(a["name"])
print(a.get("name"))

###print(a["salary"])     #shows error

print(a.get("salary"))

print(a.get("salary", 0))

print(a.keys())
print(a.values())
print(a.items())

print(len(a))
print(min(a))
print(max(a))
print(a)

a["salary"] = 100
print(a)

del a["salary"]
print(a)
'''


### Key should be always unique in dictionary

a = {"name" : "Kiran", "location" : "Chennai", "age" : "20", "name" : "test"}
print(a)

b = a.popitem()
print(a)
print(b)

a = ["one", "two", "three"]
b = [1, 2, 3]
c = dict(zip(a,b))          #zip - shortcut method to combine key value pair
print(c)
