# """if 5>2 :
#  print("five is greater than two")
# print("five is greater than two")
# """
# x=5
# x="hi there"
# print(x)

# y=str(3)
# print(type(y))
# y=int(3)
# print(y)

# y=float(3)
# print(y)

x, y, z = "orange", "banana", "apple"
fruits=["banana","lemon","orange"]
x,y,z=fruits
x="python"
y="is"
z="awesome"
print(x+' '+ y +' '+ z)
#the best way to output values is to use the comma
print(x,y,z)






"""Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

Dictionaries are written with curly brackets, and have keys and values:

"""

dictionary={
    "name":"Mohammed",
    "id":1,
    "id":1
}
#Doesn't allow duplication
print(dictionary)


#the del keyword can also delete the dictionary completely:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict
# print(thisdict)
 #this will cause an error because "thisdict" no longer exists.

 #items()	Returns a list containing a tuple for each key value pair