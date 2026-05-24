#String Data Type
from turtle import color


mystring = "This is a string."
print(mystring)
print(type(mystring))
print(str(mystring) + " is of the data type " + str(type(mystring)))
#String Concatenation
firststring = "water"
secondstring = "fall"
thirdstring = firststring + secondstring
print(thirdstring)
#Input String
name = input("What is your name? ")
print(name)
#String Formatting
color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")
print("{}, I see you like {} {}!".format(name, color, animal))