
# Upper Bound



def upper_bound(A, target):
    prev = len(A)
    for index in range(len(A)-1,0,-1):
        if A[index] == target:
            return index

        elif A[index] < target:
            return prev

        prev = index     


A = [1,1,1,2,2,5,6,6,7,7]
target = 7
print(upper_bound(A, target))