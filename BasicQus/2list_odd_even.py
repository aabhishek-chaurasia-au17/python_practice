"""
Exercise 10: Given a two list of numbers create a new list such that
new list should contain only odd numbers from the first list and 
even numbers from the second list.

list1 =  [10, 20, 23, 11, 17]
list 2 = [13, 43, 24, 36, 12]

result List is [23, 11, 17, 24, 36, 12]
"""

def add_odd(a, b):
    list3 = []
    for i in a:
        if i % 2 == 1:
            list3.append(i)
    for j in b:
        if j % 2 == 1:
            list3.append(j)
    
    return list3    


list1 = [10, 20, 23, 11, 17]
list2 = [13, 43, 24, 36, 12]

print(add_odd(list1,list2))