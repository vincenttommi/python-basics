#regEx 
#I s asequence of patterns that forms a search pattern
#can be used to check if string contains specified search pattern
#python has bult in package used to work with regular Expressions'


# import re

# txt = "the rain in spain"
# x = re.search("the rain",txt)

# if x:
#     print("yes we have a match!")
# else:
#     print("no match")


#find all function
#returns  a list containing all the  matches
#returns an empty list when no match is found

# import re

# txt = "the rain in spain"
# x = re.findall("portugal",txt)

# print(x)


    

#search function()
#searches a  string for a match and returns a match  object if there is a match
#if there is more that one match ,only first occurence of the match will be returned




#match object
# a match object is an object containing information about the search and result


# import re
# txt = "vincent learning python"

# x = re.search("py",txt)
# print(x) 
# #this will print an object


# span()
#returns  a tuple containing the start and end position of the match
# .string returns  the string passed into the function
# .group() returns the part  of the string where there was a match


import re

txt = "Tommi is learining python"
x = re.search(r"\bS\w+", txt)

print(x)
