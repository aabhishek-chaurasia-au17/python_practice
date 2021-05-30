"""
Given a string and an integer number n, remove characters from 
a string starting from zero up to n and return a new string
"""

def removeChars(str,a):
    return str[a:]

print(removeChars("pynative", 4)) 
