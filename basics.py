#Get the link of the list

thelist = ["Apple", "Banana", "Orange"]
print(len(thelist))


#int , string, boolean types
numbers=[1,50,30,20]
stringValues=["car","motorcyle","bus"]
booleanData=[True,False,True,False]

print(booleanData)

#Mixed data types
differentDataType=["string",6,True]
print(differentDataType)


#Using list constructor to make a list
newList=list(("hello","hi","there"))
print(newList)

#loop thought the items of list
# for x in newList:
#  print(x)

#loop using index
for i in range(len(newList)):
 print(newList[i])

 #while loop
 print("while")
 i=0
 while(i<len(newList)):
  print(newList[i])
  i+=1

#A short hand for loop that will print all items in a list:
  thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits =["Apple","lemon","banana"]
#newlist = [expression for item in iterable if condition == True]
newList=[x for x in fruits if "a" in x]

print(newList)


#The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".

newlist = [x for x in fruits if x != "apple"]


#Sort the list based on how close the number is to 50:

def myfunc(n):
  return abs(n - 50)

listNumbers = [100, 50, 65, 82, 23]
listNumbers.sort(key = myfunc)
print(listNumbers)

#Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


#using extend to add to the end of the previous list
thislist.extend(listNumbers)
print(thislist) 