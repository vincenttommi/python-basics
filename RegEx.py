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

import re

txt = "the rain in spain"
x = re.findall("ai",txt)

print(x)


    
