#python json
#is a systax for exchanging and storing data
#json is text,written with javascript object notation


#converting from  json to python




# import json

# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)

# # the result is a Python dictionary:
# print(y["age"])



#converting python to json
#if you have  a python object,you can convert it into  json string  by using json.dumps()


#converting from python to json
#json.dumps() we use this function  when converting python strings to json strings



import json

x = {
    "name" : "vincenttommi",
    "age": 20,
    "country":"kenya",
}

#converst into json

y = json.dumps(x)
print(x)

#The following  python objects can be converted into json strings
#list
#tuple
#sets
# string
#int
# float
#True
#False


#The format result
# 