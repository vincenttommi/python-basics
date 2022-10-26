#scope a variable is only available  from the inside region it was created

#local scope 
#a variable created inside a functuion belongs to  local scope of the function
#a  variable is available from the only region oit was created
#The variable is available for any function  inside a function
    
       





#global scope
#are variables created inside  the scope of a function of outside a function
#global variables are available  from within  any scope and global scope


x = 300

def myfunc():
    print(x)
    
    
myfunc()
print(x)



x = "vincentommi"

def myfunc():
    print(x)
    
    
myfunc()    