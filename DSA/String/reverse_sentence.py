# Reverse words in a given String in Python

"""
Input : str = geeks quiz practice code
Output : str = code practice quiz geeks
"""

def Reverse_string(a):
    
    word = a.split(' ')
    word = ' '.join(reversed(word))
    return word
    

if __name__ == "__main__":

    str = "geeks quiz practice code"
    print(Reverse_string(str))

