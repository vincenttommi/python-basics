# global variables 
# created outside a function and can be accessed both outside and inside the function
x  = "awesome"

def myfunc():
    x  = "is  cool"
    print("python is "  + x)
   
myfunc() 
print("coding python is " + x)    
    
    


