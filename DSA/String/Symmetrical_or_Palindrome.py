# Python program to check whether the string is Symmetrical or Palindrome
"""
Input: khokho
Output: 
The entered string is symmetrical
The entered string is not palindrome

Input:amaama
Output:
The entered string is symmetrical
The entered string is palindrome
"""

print("-------------- try ------------")


def SymmetricalorPalindrome(x):

    ans = ""

    for i in x:
        ans = i + ans

    if x == ans:
        print("The entered string is symmetrical \n The entered string is palindrome")
    else:
        print("The entered string is symmetrical \n The entered string is not palindrome")
    

if __name__ == "__main__":

    x = "amaama"
    SymmetricalorPalindrome(x)

