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






"""
Set
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.
"""
"""Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.

Once a set is created, you cannot change its items, but you can remove items and add new items.
"""

#Duplicates Not Allowed
#Sets cannot have two items with the same value.
duplicateExample={"apple","banana","apple"}
print(duplicateExample)