# Python | Count the Number of matching characters in a pair of string
"""
Input : str1 = 'abcdef'
        str2 = 'defghia'
Output : 4 
(i.e. matching characters :- a, d, e, f)

Input : str1 = 'aabcddekll12@'
        str2 = 'bb22ll@55k'
Output : 5 
(i.e. matching characters :- b, 1, 2, @, k)
"""
print("-------------- my approch ------------------")

def maching(a,b):
    
    count = 0
    for i in a:
        for j in b:
            if i == j:
                count += 1
    print(count)

if __name__=="__main__":

    str1 = 'aabcddekll12@'
    str2 = 'bb2211@55k'
    maching(str1,str2)

print("----------------- try ----------------")


import re
str3 = 'abcdef'
str4 = 'defghia'
        
c = 0
for i in str3:
    if re.search(i,str4):
        c=c+1

print(c)

