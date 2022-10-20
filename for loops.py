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


fruits = ["apple","banana","grapes","orange","beans"]

for x in fruits:
 if x == "orange":
     continue
 print(x)
    