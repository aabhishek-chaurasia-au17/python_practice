# Find length of a string in python (4 ways)

"""
Input : 'abc'
Output : 3

Input : 'hello world !'
Output : 13

Input : ' h e l   l  o '
Output :14
"""

def lenthofstring(str):
    
    a = len(str)
    return a 

if __name__ == "__main__":
    str ='hello world !'
    print(lenthofstring(str))



def stringlenth(s):

    count = 0
    for i in s:
        count += 1
    
    return count


if __name__ == "__main__":

    s = ' h e l   l  o '
    print(stringlenth(s))