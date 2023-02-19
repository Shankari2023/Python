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
print(a.index("a", 2))
print(a.index("a", 2, 14))
# print(a.index("z"))

#it shows error message because its requesting to find the value that is not in the given string.
#Avoiding error message while writing program.
#To avoid this error message we can go for
#find and rfind
#find and index is the same - unless find returns -1 if the substring is not found

a = "SachinTendulkar"
print(a.index("n"))
print(a.find("n"))
print(a.find("z"))

print(a.rindex("n"))
print(a.rfind("n"))
print(a.rfind("z"))

print(a.rindex("n"))
print(a.rindex("a"))
print(a.rindex("z"))