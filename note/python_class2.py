# Given 2 numbers, check if they are divisible by each other. Return True if yes, False if no

# either a is divisible by b or b is divisible by a.

# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")

# num1 = int(num1)
# num2 = int(num2)
# print(num1%num2==0)

# num1 is divisible by num2, num1%num2
# bool(num1%num2) = False

# 13 % 7 = bool(6) = True


# num2 is divisible by num1, num2%num1
# bool(num2%num1)

# print(num1%num2==0 or num2%num1==0)
# print((not bool(num1%num2)) or (not bool(num2%num1)))

# print(5==8)

"""
1. variable
2. 4 basic datatypes: integer/number, string/text, float/decimals, boolean/true and false

integer: int
float: float 
boolean: bool 
string: str

3. print()
end with print
, with print
escape characters: \n (enter) and \t (tab)

4. type()
returns the type of value a variable is storing

print(type(variable_name))

5. type casting or type conversion : to change the data type of the value 

int to string, string to int 
int to float, float to int
int to boolean, boolean to int
float to string, string to float 
float to boolean, boolean to float
string to boolean, boolean to string
"""

# pr = 5
# print(pr, type(pr))
# pr = "My Name is Priyesh"
# print(pr, type(pr))
# pr = "523042434"
# print(pr, type(pr))
# pr = 12.3452
# print(pr, type(pr))
# pr = True 
# print(pr, type(pr))
# pr = False 
# print(pr, type(pr))

# 1.int to string, string to int 

# pr = 5
# print(pr, type(pr))
# pr = str(pr)
# print(pr, type(pr))
# print()
# pr = "2134942034"
# print(pr, type(pr))
# pr = int(pr)
# print(pr, type(pr))
# error case: string contains things apart from digits
# err = "My Name is Priyesh 123"
# print(err, type(err))
# err = int(err)
# print(err, type(err))

# 2. int to float, float to int

# pr = 5
# print(pr, type(pr))
# pr = float(pr)
# print(pr, type(pr))
# print()
# pr = 5.9234
# print(pr, type(pr))
# pr = int(pr)
# print(pr, type(pr))

# 3. int to bool, bool to int
# pr = 5
# print(pr, type(pr))
# pr = bool(pr)
# print(pr, type(pr))
# non zero numbers will become true when converted to boolean
# pr = False
# print(pr, type(pr))
# pr = int(pr)
# print(pr, type(pr))

# 4. float to string, string to float

# pr = 5.91234
# print(pr, type(pr))
# pr = str(pr)
# print(pr, type(pr))
# print()
# pr = "8.342442"
# print(pr, type(pr))
# pr = float(pr)
# print(pr, type(pr))
# error case: string contains things apart from digits
# err = "123.12.1234sfggrffbrbg"
# print(err, type(err))
# err = float(err)
# print(err, type(err))

# 5. float to boolean, boolean to float
# pr = 5.91234
# print(pr, type(pr))
# non zero numbers will become true when converted to boolean
# pr = bool(pr)
# print(pr, type(pr))
# pr = 0.0
# pr = bool(pr)
# print(pr, type(pr))
# pr = -100.10
# pr = bool(pr)
# print(pr, type(pr))

# 6.string to boolean, boolean to string

# pr = "True"
# print(pr, type(pr))
# pr = bool(pr)
# print(pr, type(pr))
# pr = "False"
# print(pr, type(pr))
# pr = bool(pr)
# print(pr, type(pr))
# All non empty string will give true, empty string will give False
# pr = "My Name is Priyesh"
# print(pr, type(pr))
# pr = bool(pr)
# print(pr, type(pr))
# pr = ""
# print(pr, type(pr))
# pr = bool(pr)
# print(pr, type(pr))

# pr = True
# print(pr, type(pr))
# pr = str(pr)
# print(pr, type(pr))

# Users(runs a program) and programmers(writes a program).

# Programmer required some input from your side while running the program. In arcade games, your name. 

# it is possible that you might want to ask the user for input at runtime.

# input() command in python
inp = input("I want to know your age? ")
# inp = int(inp)
print(inp, type(inp))

# inp = 21 [not the correct thing]
# inp = "21" [correct]