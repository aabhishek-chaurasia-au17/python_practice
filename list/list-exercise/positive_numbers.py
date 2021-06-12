# Python program to print positive numbers in a list
"""
Input: list1 = [12, -7, 5, 64, -14]
Output: 12, 5, 64

Input: list2 = [12, 14, -95, 3]
Output: [12, 14, 3]
"""
def find_positive(a):

    for i in a:
        if i > 0 or i == 0:
            print(i , end=" ")



list1 = [12, -7, 5, 64, -14]
find_positive(list1)