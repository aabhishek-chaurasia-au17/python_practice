"""
Python is basically a programming language that allows you to instruct a computer in a manner that humans can understand.

Programming Languages have to follow a certain set of rules called syntax so that it is computer readable.

Since, computers can only understand 0s and 1s, we will write our code in a file in python language which contain instructions for the computer. A program called the interpreter will convert line by line into 0s and 1s for the computer to understand.

Python was invented in 1994 by Guido Van Rossum, bored of other languages. Tedious Syntax.

Linux has been written using the C programming language.

Machine Learning, Data Science

since python is easy to run, need to write very less code for the same task and has a lot of 3rd party libraries/software. Python is like a swiss knife in CS. 

Python 3.8.2 - fixed python version
"""

# Print : just displays the same message on the screen as what you have entered

# print("Hello World")

"""
to run a python file: open the terminal and type python3 <file_name>
"""

# print("Hello World", "My Name is Priyesh")

# print("Hello World", end=", ")
# print("My name is Priyesh")

# print("Hello World")
# print("My name is \t Priyesh")

# on the keyboard, there are a few characters which cannot be printed directly on the screen, so they have special representations

# \t: tab key
# \n: enter key

# print("Priyesh", end = " ")
# print("Priyesh", end = " ")
# print("Priyesh", end = " ")
# print("Priyesh", end = " ")
# print("Priyesh")

# print("Priyesh "*5)

# Variables

# Work with dynamic values
# you need to keep track of the memory location where the values are stored.

# Variable is a pointer/placeholder/container that points to a particular location in your RAM which has a certain data. 

# Integer => Numbers
# String => Text
# Decimal => Float
# Boolean (True or False)

# x = 5
# print("Value of x is: ", x)
# x = True
# print("Value of x is: ", x)
# x = False 
# print("Value of x is: ", x)
# x = 7.8324823
# print("Value of x is: ", x)
# x = "My Name is Priyesh" 
# print("Value of x is: ", x)

# Advantage of variables is to store and reuse data or previous results in the program. 

a = 10
b = 5
c = a+b

# print(c+2)
# print(c*12)
# print(c+"2")
# In python " and ' are exactly equal, no difference at all

# sudo apt-get update python3

# 2 + "123"
# "123" + 2
# print("2" , "123")
# print("My age is: " + "18" + " years")

# Take User Input
age = input("Please enter your age: ")

# in order to take user input, use the input() command
# result of this command needs to be stored in a variable
# so that later on, it can fetched for reuse 

# input() or input("Message")

# print("The age entered by the user is: ", age)

# Any data input from the user using input() will be text data by default.

# print("My Name is \\n priyesh")

# type() - function takes a variable and tells you what type of value the variable is storing

# x = 5
# print("Value of x is: ", x)
# x = True
# print("Value of x is: ", x)
# x = False 
# print("Value of x is: ", x)
# x = 7.8324823
# print("Value of x is: ", x)
# x = "My Name is Priyesh" 
# print("Value of x is: ", x)