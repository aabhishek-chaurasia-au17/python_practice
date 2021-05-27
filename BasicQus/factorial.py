# Factorial of a non-negative integer, is multiplication of all 
# integers smaller than or # equal to n. For example factorial
# of 6 is 6*5*4*3*2*1 which is 720.

# import math

# def myfactorial(a):
#     return math.factorial(a)

# num = 5 
# print(myfactorial(num))

# -----------------------------------------------------------------


def factorial(n):

    return 1 if n==1 or n==0 else n* factorial(n-1)

num = 4
print(factorial(num))    