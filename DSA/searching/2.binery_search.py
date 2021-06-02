# Binery Search
"""
binery search is works only for sorted solution Space/list.
"""

# A = [1,22,44,55,66,77,88,120,151]

# target = 88

# def binery_search(A, target):

#     left = 0
#     right = len(A)-1

#     while left <= right:
#         mid = (left+right)//2

#         if A [mid] == target:
#             return mid
#         elif A[mid] > target:
#             right = mid -1
#         else:
#             left = mid -1        

#     return None

# A = [1,22,44,55,66,77,88,120,151]

# target = 88

# print(binery_search( A, target))



def binery_search(a, target):
    left = 0
    right = len(a)-1
    
    while left < right:
        mid =(left + right)//2
        
        if a[mid] == target:
            return mid
        elif a[mid] > target:
            right = mid -1
        else:
            left = mid -1
    
        return None        


a = [1,2,3,4,5,6,7]
target = 4

print(binery_search(a, target))