# global variables 
# created outside a function and can be accessed both outside and inside the function
# in above two variables are created one outside using the same name and another inside 
# accesed in the same function but bring different outcome
x = "progamming language"

def myfunction():
    print("python is an easier" + x)
    
myfunction()
print("Learning a " + x)    


