# adding items in a set
# we use add()




# thisset = {"apple","banana","cherry"}
# thisset.add("orange")

# print(thisset)

#adding set to another function we use  the update method


# thisset = {"apple","banana","cherry"}
# tropical = {"mango","grapes","papaya"}


# thisset.update(tropical)
# print(thisset)


# marks = {100,200,300,400,500,600,700}
# marks2 = {20,34,50,60,70,80,90}

# marks.update(marks2)
# print(marks)

#add any iterable
#object in update function does not have to be set it can be tupples or list and dictionaries

thisset = {"apple","banane","cherry"}
mylist = {"kiwi","orange"}

thisset.update(mylist)
print(thisset)
