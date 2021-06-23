# Remove all duplicates from a given string in Python
"""
Input : geeksforgeeks
Output : efgkos
"""

def Remove_duplicates(str):
    
    # s = set(str)
    # s = "".join(s)
    # print("without order:",s)
    t=""
    for i in str:
        if i in t:
            pass
        else:
            t += i
    
    return t    
    

if __name__=="__main__":

   str = "geeksforgeeks"
   print(Remove_duplicates(str))