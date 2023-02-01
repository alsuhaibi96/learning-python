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






"""Tuple
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
"""

#Tuple is used to a collection which is ordered and unchangable
#Tuples are written with round brackets.
thisTuple=("hello","there")
print(thisTuple)


#One item tuple, remember the comma:


#In Python ! Is this tuple ? 
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#Negative indexing means starting from the end of the tuple.

#This example returns the items from index -4 (included) to index -1 (excluded)

#Remember that the last item has the index -1,

