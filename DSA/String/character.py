# Ways to remove i’th character from string in Python

"""
The original string is : GeeksForGeeks
The string after removal of i'th character : GeksForGeeks
"""

def remove_character(a):

    b = len(a)
    new_str = ""

    for i in range(b):
        if i != 2:
            new_str = new_str + a[i]
            
    return new_str

if __name__ == "__main__":

    str =  "GeeksForGeeks"
    print(remove_character(str))
