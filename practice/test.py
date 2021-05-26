
# num = 2
# i = 0

# while i < 10:
#     i+=1
#     print(num * i)


# for i in range(2,20+1,2):
#     print(i)

# num = 2 
# for i in range(1,11,1): 
#     into = i * 2 
#     print(into)




# list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

# for i in list1:

#     if i > 150:
#         break
#     elif i % 5 == 0:
#         print(i)


# """
# Question 1. 
# Write a program using recursion to countthe number ofvowels in a string.
# """

# sentence = input("Enter One Line: ")
# string = sentence.lower()
# count = 0
# list = ["a", "e","i","o","u"]

# for i in string:
#     if i in list:
#         count = count +1

# print(f"Vowels are in sentance: {count} ")

"""
Question 2. 
Write a program to find the fibonaccinumber in a string.
"""

def fib(n):
    a = 0
    b = 1

    print(a)
    print(b)

    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)

fib(5)
