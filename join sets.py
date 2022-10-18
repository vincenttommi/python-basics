#Joining two sets
#we use union() returns a new set with all items from the set


# set1 = {"a","b","c"}
# set2 = {1,2,3}

# set3 = set1.union(set2)
# print(set3)

#update() inserts items of set1 into set2


# set1 = {"a","b","c","c"}
# set2 = {1,2,3}


# set1.update(set2)

# print(set1)
 
#  the intersection_duplicates
#keeps items that are  present in  both sets.
#intersection_update()




# x = {"apple","banana","cherry","google"}
# y = {"google","microsoft","apple"}


# x.intersection_update(y)

# print(x)

# x = {"apple","google","microsoft","cherry","sadiomane"}
# y = {"apple","sadiomane","cherry","sadiomane"}


# x.intersection_update(y)

# print(x)
 
#  Keep All, But NOT the Duplicates
# symmetric_difference_update() keeps elements that are not both in all sets.

# x = {"apple","banana","grapes","mango"}
# y = {"avacado","microsoft","google","twitter"}



# z = x.symmetric_difference(y)

# print(x)


names = {"sadiomane","stevengerald","mango","banana"}
names2 = {"avacado","banana","mango","google"}


names3 = names.symmetric_difference(names2)

print(names)