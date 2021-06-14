# Sort the values of first list using second list in Python
"""
Input : list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

Output :['a', 'd', 'h', 'b', 'c', 'e', 'i', 'f', 'g']


Input : list1 = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]
        list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

Output : ['g', 'k', 'r', 'e', 'e', 'g', 's', 'f', 'o']

"""

def sort_value(a,b):
    
    a_zip = zip(b, a)
    
    z = [x for _, x in sorted(a_zip)]

    return z
        
if __name__=="__main__":
    
    list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    list2 = [ 0,   1,   1,   0,   1,   2,   2,   0,   1]

    print(sort_value(list1,list2))


# def sort_list(list1,list2):

#     zip_list = zip(list2,list1)
    
#     z = [a for _, a in sorted(zip_list)]

#     return z 

# x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
# y = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
 
# print(sort_list(x, y))