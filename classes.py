#python classess and objects
#a class is alike an object constructor
# class myclass:
#     x = 5
# print(myclass)    



# class myclass:
#     x=5
    
# p1 = myclass()
# print(p1.x)    


# The_str_()function
#controls what should be returned  when the class object is  reprsented as a string
#the string_str_function is not set but  is returned


class Person:
      def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)
