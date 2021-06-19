# Python | Check if a Substring is Present in a Given String
"""
Input : s1 = geeks s2=geeks for geeks
Output : yes

Input : s1 = geek s2=geeks for geeks
Output : yes
"""


def substring(a, b):
    
    if (a.find(b) == -1):
        print("no")
    else:
        print("yes")    

if __name__ == "__main__" :
    
     
    s2 = "hi for abhi"
    s1 = "abhi"
    substring(s2,s1)    


