"""
Given a range of the first 10 numbers, Iterate from the start 
number to the end number, and In each iteration print the sum 
of the current number and previous number
"""

# for i in range(0,10):
#     print(f"Current Number {i} Previous Number{i-0} Sum: {i+i}")

def iterate(num):
    pre = 0
    for i in range(0,num):
        sum = pre + i
        print(f"Current Number {i} Previous Number {pre} Sum: {sum}")
        pre = i

iterate(10)