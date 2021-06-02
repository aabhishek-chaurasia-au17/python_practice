# Given an array (or string), the task is to reverse the array/string.

"""
Input  : arr[] = {1, 2, 3}
Output : arr[] = {3, 2, 1}

Input :  arr[] = {4, 5, 1, 2}
Output : arr[] = {2, 1, 5, 4}
"""

def reverse(n):
    return [i for i in reversed(n)]
arr = [1, 2, 3]
print(reverse(arr))


def reverse_arry(A):
    print(A[::-1])

# A = [1,2,3,4,5,6]
A = ["A","B","H","I","S","H","E","K"]
reverse_arry(A)



# start = 0 
# end = len(A)-1 

# def reverse_strarry(A,start,end):
#     while start < end:
#         A[start],A[end] = A[end],A[start]
#         start +=1
#         end -=1

# # A = ["A","B","H","I","S","H","E","K"]
# A = [1,2,3,4,5,6]
# print(reverse_strarry(A,start,end))