# Python program to print all even numbers in a 
"""
Input: start = 4, end = 15
Output: 4, 6, 8, 10, 12, 14

Input: start = 8, end = 11
Output: 8, 10
"""

# for i in range(4,15,2):
#     print(i, end=" ")


for i in range(4,15):
    if i % 2 == 0:
        print(i, end=" ")
