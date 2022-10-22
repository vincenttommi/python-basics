#function is a block of code that which runs when called.
#you can pass data,known as parameters,into function


#creating a function in python


# def myfunction():
#     print('welcome vincenttommi')
    
# myfunction()    



#arguments
#information can be passed into functions as arguments
#arguments are specified after the function name,inside parenthess.you can add as many arguments as you want


# def my_function(fname):
#       print(fname + "company")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")
#arguments are always shortened to arg in python


# def my_function(fname):
#     print(fname + "tommi")

    
    
# my_function("vincent")
# my_function("vin")
# my_function("korir")

#By default a function must be called with exact number of arguments
#meaning if your function expects 2 arguments you have to call to functions with two argumnets



    

# def my_function(fname,lname):
#     print(fname +  "" + lname)
    
#     my_function("vincent", "tommi")

#key arguments in python

 



# def myfunction(child3, child2, child1):
#     print("the youngest chils is" + child3)
    
# myfunction(child1 = "vincent", child2 = "brayo", child3 = "Lilo")    



#arbitray keword in python
# helps to capture unkwon double amount of parameter  passed in a function

# def my_function(** kid):
#     print("His last name is " + kid["lname"])
    
# my_function(fname = "vincent", lname = "tommi") 




# def functeams(** club):
#     print("my favourite team is " + club["name"])
    
    
    
# functeams(name = "chelsea", nicknames = "The blues")



#Default parameter  value
#if we call a function without an argument , it uses the default value


# def my_function(country = "norway"):
#     print("I am from " + country)
    
    
    
    
# my_function("sweden") 
# my_function("india")
# my_function()
# my_function("Brazil")   



#passing a list as an argument
#it allows sending  of data types  of arguments to a function(list,tuple,dictionary)
#thus treated as any other data.


def myfunction(teams):
    for x in teams:
        print(x)
        
        
countries = ["England","Germany","Australia","Canada"]


myfunction(countries)         

