# Python Program to find sum of array

"""
Given an array of integers, find the sum of its elements.

Examples :

Input : arr[] = {1, 2, 3}
Output : 6
1 + 2 + 3 = 6

Input : arr[] = {15, 12, 13, 10}
Output : 50
"""

def sum_arry(arr):
    sum = 0

    for i in arr:
       sum += i
    return sum

arr = [15, 12, 13, 10]
print(sum_arry(arr))   