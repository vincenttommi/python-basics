#changing values 
#you can change value of a specific item by reffering to its name


#update() will update  dictionary with items from given arguments

thisdict = {
    
    "Brand" : "Ford",
    "Model" :"Mustang",
    "year" : "1964",
    
}

thisdict.update({"year" : 2022})

print(thisdict)

