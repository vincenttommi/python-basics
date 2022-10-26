#scope a variable is only available  from the inside region it was created

#local scope 
#a variable created inside a functuion belongs to  local scope of the function


def myfunc():
    x = 300
    print(x)
    
    
myfunc()    
    