# Python – Convert Snake case to Pascal case
"""
Input : geeks_for_geeks
Output : GeeksforGeeks

Input : left_index
Output : leftIndex
"""

def convertpascal(a):
    for i in a:
        if i != "_":
            print(i,end="")


if __name__ == "__main__":

    str = "geeks_for_geeks"
    convertpascal(str)


def Pascalcase(a):
    for i in a:
        if i != "_":
    
            print(i, end="")

if __name__=="__main__":

    s = "left_index"
    Pascalcase(s)