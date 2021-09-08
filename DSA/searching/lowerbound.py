
# lower bound
"""
Lower bound is first just smaller Value in left or lewest
index some value.
"""



def lower_bound(A, target):

    prev = 0
    for index in range(len(A)):
        if A[index] > target:
            return prev-1

        else:
            prev = index    

A = [1,1,1,2,2,5,6,6,7]

target = 6
print(lower_bound(A, target))