
# Python | Program to accept the strings which contains all vowels

"""
Input : geeksforgeeks
Output : Not Accepted
All vowels except 'o' are not present

Input : ABeeIghiObhkUul
Output : Accepted
All vowels are present
"""


def find_vowel(s):

    s = s.lower()

    vowels = set("aeiou")
    a = set({})
    for i in s:
        if i in vowels:
            a.add(i)
        else:
            pass


    if len(a) == len(vowels):
        print("Accepted")
    else:
        print("Not Accepted")

    
if __name__=="__main__":

    str = "abhiosaeiouhek"
    find_vowel(str)
