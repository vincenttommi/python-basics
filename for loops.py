#for loops in python
#a for loop is used in iterating over a sequence
# either tuple,list , set ,dictionary or string thus showing output inside values
#forloop does not require an indexing variable to set beforehand

# fruits = ["banana","cherry","grapes","orange"]

# for x in fruits:
#     print(fruits)

#using for loop to iterate over strings


# for x in "banana":
#     print(x)

#break statement in for loop 
#used to stop loop before it has looped through both items


# fruits = ["tomato","mango","banana","apple","cherry","grapes"]

# for x in fruits:
#     print(x)
#     if x=="banana":
#      break    

#example 2 
#break comes before print

# fruits = ["apple","banana","cherry"]

# for x in fruits:
#     if x == "banana":
#         break
#     print(x)   

#continue statement in forloop
#with continue statement we can stop current iteration then continue with the next


# fruits = ["apple","banana","grapes","orange","beans"]

# for x in fruits:
#  if x == "orange":
#      continue
#  print(x)
    
    
#range()
#used to loop  a set of code through a number of  times
#returns  a sequence of number from 0 by default  and increments by 1


# for x in range(2,6):
#     print(x)

#else in forloop
# specifies a block of code to be excuted when the block is finished


# for x in range(2,10):
#     print(x)
# else:
#     print("finally finished")


# for x in range(6):
#     if x == 3:break
#     print(x)
# else:
#     print("finally finished")   


#nested loops
#Is a loop inside aloop.
#inner loop will be excuted one time for each iteration of outer loop


clubs = ["manchester united","chelsea","stokecity","totehnam"]

captains = ["aziplicueta","maguire","unknown","Hugo loris"]


for x in clubs:
    for y in captains:
            print(x,y)