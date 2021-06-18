# Python program to check if a string is palindrome or not

"""
Input : malayalam
Output : Yes

Input : geeks
Output : No
"""

print("--------------- try 1 ---------------------")

def palindrome(s):
    return s == s[::-1]


if __name__=="__main__":

    s = "malayalam"
    ans = palindrome(s)

    if ans:
        print("Yes")
    else:
        print("No")


print("--------------- try 2 ---------------------")


x = "abhishek"

y = ""

for i in x:
    y = i + y

if x == y:
    print("yes")

else:
    print("no")    



