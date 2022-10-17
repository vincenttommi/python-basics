#customize sort function()
#you can customize your function using key argument key = function
#The function will return a number that would be used to sort a list

def myfunc(n):
    return abs(n - 50)

numbers = [100,40,50,80,90,56,78,90,200,300]
numbers.sort(key = myfunc)
print(numbers)

