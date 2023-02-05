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


#using the functions and the global variables
# x="awesome"

# def myFunc():
#      global x
#     x="fantastic"
#     print("the x value is",x)

# myFunc()
# print("the global variable is ",x)




#Add 10 to argument a, and return the result:

x = lambda a : a + 10
print(x(5))

#using lambda for giving the power of any number

def powerMethod(n):
   return lambda a:a*n

myDoubler =powerMethod(2)
print(myDoubler(12))
