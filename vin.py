#string formats
#we comnine numbers and string using  format()
#inserts numbers into strings
#Takes unlimited number of arguments and replaces it repectively





quantity = 3
itemno = 537
price = 50.34
myorder = "I want to pay  {2} dollars for {0}pieces of item {1}. "
print(myorder.format(quantity,itemno,price))

