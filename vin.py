#changing a range of item values
#define a list with new values  and refer to the range of index numbers  where you want to insert the new values.

thislist = ["apple","banana","cherry","orange","kiwi","mango"]
thislist[-1:-5] = ["watermelon","grapes"]
print(thislist)
