# Python | Program to print duplicates from a list of integers

"""
Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
Output : output_list = [20, 30, -20, 60]


Input :  list = [-1, 1, -1, 8]
Output : output_list = [-1]
"""

def duplicates(x):
    size = len(x)
    output_list = []
    for i in range(size):
        k = i + 1
        for j in range(k,size):
            if x[i] == x[j] and x[i] not in output_list:
                output_list.append(x[i])
    
    return output_list            

    

if __name__=="__main__":
    list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
    
    print(duplicates(list1))
