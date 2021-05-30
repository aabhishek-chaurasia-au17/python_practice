"""
Given a list of numbers, return True if first and last number 
of a list is same.
"""
# ex:
# Given list is  [10, 20, 30, 40, 10]
# result is True

# Given list is  [10, 20, 30, 40, 50]
# result is False

def lastNum(a):
    firstnum = list1[0]
    lastnumb = list1[-1]

    if firstnum == lastnumb:
        return True
    else:
        return False    

list1 = [10, 20, 30, 40, 10]

print(lastNum(list1))