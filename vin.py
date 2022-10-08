#global keyword
# used for creating a global variable inside a function
# changing value of global keyword inside a function  we refer to the variable  by using globalkeyword

x = "cool"

 
def myfunction():
    global x 
    x = "great"
myfunction()
print("python is " + x)    