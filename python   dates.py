# date in python is not a datatype of its own  but we can import a module of  named date time to work as 
# dates as objects


# import datetime

# x = datetime.datetime.now()


# print(x)



# #returning year and name of the week

# import datetime

# x = datetime.datetime.now()
# print(x.year)

# print(x.strftime("%A"))


#creating date objects in python


#To create a date  wes uses datetime() constructor
#datetime() requires three parameters to create a date:year,month,day



import datetime

x = datetime.datetime(2022,10,26)

print(x)