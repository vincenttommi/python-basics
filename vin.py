#python identity operators
#are used to compare objects  not if they are equal but if they are actually the same with same memory location
x = ["apple","banana"]
y = ["apple","banana"]

z = x

print( x is z)
#returns true because x is the same object as  z
print( x is y)
#returns false because x is  not the same object as y ,yet they have the same values
print(x == y)
#Demonstrates difference btn "is" and "=" returns true since its equal to y
