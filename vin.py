#Exending list in python
#To append list from another list to current  list we use extend()
#nicknames adds elements to names


#adding any iterable
#the extend method does not have to  append list  you  can add any iterable object  tuples ,sets ,dictionaries

#adding  elements of a tupple to a list
thislist = ["apple","banana","cherry"]
thistuple = ["kiwi","orange"]
thislist.extend(thistuple)
print(thislist)
