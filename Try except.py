#try lets you test a  block of code 
# except blocks lets you  handle the error
# else block helps one excute the code when there  is no error
#finally lets you excute the block regardless  of the result






# try:
    
#     print(x)
# except NameError:
#     print("variable x is not defined")
# except:
#     print("something else went wrong")    



#else you can use the else keyword to define the block of code to be excuted


# try:
#     print("hello world")
# except:
#     print("something went wrong")
# else:
#     print("nothing went wrong")    
    
    
    
#try block does not generate an error

#finally block
#if specified will be excuted regardless if the try block raises an  error
# try:
#     print(x)
# except:
#     print("something went wrong") 
    
# finally:
#     print("The try except is finished")
        
        
        
        
        
# try:
#     f = open("demofile.txt")
# try:
#     f.write("lorem ispum")
# except:
#     print("something went wrong when writing into a file")
# finally:
#     f.close() 
# except:
#     print("something went wrong when opening the file")   
           
        
        
        
        
        
        
#raising exception
#raise an error and stop a program if x is lower than 0

x = -1
if x < 0:
    raise Exception("sorry,no numbers below zero")
