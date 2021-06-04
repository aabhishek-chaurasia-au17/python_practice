"""
Write a code to extract each digit from an integer, in the reverse order
"""
# If the given int is 7536, the output shall be '6 3 5 7", with a space separating the digits.

def reverse(A):
    
    while A > 0:
        digit = A % 10
        A = A // 10
        print(digit, end=" ")

A = 7536
reverse(A)  