# Python – Vertical Concatenation in Matrix

"""
Input : [[“Gfg”, “good”], [“is”, “for”]]
Output : [‘Gfgis’, ‘goodfor’]
Explanation : Column wise concatenated Strings, “Gfg” concatenated with “is”, and so on.

Input : [[“Gfg”, “good”, “geeks”], [“is”, “for”, “best”]]
Output : [‘Gfgis’, ‘goodfor’, “geeksbest”]
Explanation : Column wise concatenated Strings, “Gfg” concatenated with “is”, and so on.
"""

def Vertical(x):

    res =[]
    N = 0
    while N != len(x):
        temp = ""
        for idx in x:
            try: temp = temp + idx[N]
            except IndexError: pass

        res.append(temp)
        N = N +1

    res = [ele for ele in res if ele]

    print((res))    

if __name__=="__main__":
    x = [["Gfg", "good"], ["is", "for"]]
    Vertical(x)
