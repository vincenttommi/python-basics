#is an object that contains number of countable  values
#an iterator is an onject that can iterated upon
#uses the following method _ter_() and _next_()




# myscores = (20,30,40,50,60,70,80)
# myit = iter(myscores)

# print(next(myit))
# print(next(myit))
# print(next(myit))


#strings are iterable objects and can return  an iterator


# mystr = "banana"
# myit = iter(mystr)


# print(next(myit))
# print(next(myit))
# print(next(myit))



# #looping thgrough an iterator

# mytuple = "vincent"

# for x in mytuple:
    
#     print(x)


#class iterators that return numbers

class Mynumbers:
    
    def __iter__(self):
        self.a = 1
        return self
    
    
    def __next__(self):
     x = self.a
     self.a +=1
     return x 
myclass = Mynumbers()
myiter = iter(myclass)


print(next(myiter))
print(next(myiter))
print(next(myiter))
     
     
     
     
     
     
#stop iteratio   
#prevents a statement from excuting forever


class mynumbers:
    def __iter__(self): 
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
         x = self.a
        self.a +=1 
        return x
    else:
        raise StopIteration
            \