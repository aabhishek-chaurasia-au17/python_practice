# Python program to print even length words in a string

"""
Input: s = "This is a python language"
Output: This
        is
        python
        language 

Input: s = "i am muskan"
Output: am
        muskan
"""

def evenword(s):

    s = s.split(' ')

    for i in s:
        if len(i)%2 == 0:
            print(i)

if __name__ == "__main__":

    s = "This is a python language"
    evenword(s)
