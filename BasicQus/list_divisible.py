"""
Given a list of numbers, Iterate it and print only those numbers 
which are divisible of 5
"""

# Given list is  [10, 20, 33, 46, 55]
# Divisible of 5 in a list
# 10
# 20
# 55

def divisible(a):

    for i in a:
        if i % 5 == 0:
            print(i)

lists = [10, 20, 33, 46, 55]
divisible(lists)