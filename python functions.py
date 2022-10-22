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



    

def my_function(fname,lname):
    print(fname +  "" + lname)
    
    my_function("vincent", "tommi")