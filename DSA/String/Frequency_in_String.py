# Python – Words Frequency in String Shorthands

"""
Input : test_str = ‘Gfg is best’
Output : {‘Gfg’: 1, ‘is’: 1, ‘best’: 1}

Input : test_str = ‘Gfg Gfg Gfg’
Output : {‘Gfg’: 3}
"""

def find_Frequency(a):

    res = {key: a.count(key) for key in a.split()}

    return res    

if __name__ == "__main__":
    test_str = "Gfg abhi is abhi best"
    print(find_Frequency(test_str))