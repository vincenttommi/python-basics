#python json
#is a systax for exchanging and storing data
#json is text,written with javascript object notation


#converting from  json to python




import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])