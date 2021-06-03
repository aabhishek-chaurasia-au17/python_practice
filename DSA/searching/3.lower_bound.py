# Lower Bound
"""
Lower bound is first just smaller value in left or lower index 
some value. 
"""
# Find a Lower Bound

def lower_bound(A, target):
    prev = -1
    for i in range(len(A)):
        if A[i] == target:
            return i
        elif A[i] > target:
            return prev
        prev = i
       

A = [1,1,1,2,2,5,6,6,7]
target = 8

print(lower_bound(A, target))
