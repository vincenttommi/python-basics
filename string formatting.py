#string format()
#allows one to format selected parts of a string


# meangrade=" 70.0"
# txt = "your mean grade is {} credit"

# print(txt.format(meangrade))




#multiple values 
#if you want to use  more value just add  more values to format() method


quantity = 3
itemno = 567
price = 49 

myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity,itemno,price))



