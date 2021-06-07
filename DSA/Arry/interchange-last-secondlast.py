"""
Python program to swap two elements in a list

Given a list in Python and provided the positions of the elements, 
write a program to swap the two elements in the list.
Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]
"""

def swaplast(list, pos1, pos2):
    
    list[pos1], list[pos2] = list[pos2], list[pos1]
    
    return list


List = [1, 2, 3, 4, 5]
pos1 = 2 
pos2 = 5
print(swaplast(List, pos1-1, pos2-1))    