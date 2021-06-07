# Python program to interchange first and last elements in a list
"""
Given a list, write a Python program to swap first and last element of the list.
"""

def interchange(a):
    size = len(a)
    
    temp = a[0]
    a[0] = a[size-1]
    a[size-1] = temp

    return a

list = [18, 35, 9, 56, 54, 25]
print(interchange(list))


print()


def interchangelastfirst(a):
    
    a[0],a[-1] = a[-1],a[0]

    return a

list2 = [12, 35, 9, 56, 24]
print(interchangelastfirst(list2))