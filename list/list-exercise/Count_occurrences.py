
# Python | Count occurrences of an element in a list

"""
Input : lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
         x = 10
Output : 3 
10 appears three times in given list.

Input : lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
        x = 16
Output : 0
"""
def Count_element(a,x):
    
    count = 0
    for i in a:
        if i == x:
            count += 1 
    return count    


if __name__=="__main__":
    lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
    x = 10
    print(Count_element(lst,x))


