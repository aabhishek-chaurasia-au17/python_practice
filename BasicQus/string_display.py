"""
Given a string, display only those characters which are present 
at an even index number.
"""
# my aproch
# def string(a):
#     ab = a[::2]
#     print(ab)

# str1 = "pynative"
# string(str1)

def printIndexChar(str):
    for i in range(0, len(str)-1,2):
        print(str[i])

inputstr = "pynative" 
printIndexChar(inputstr)   