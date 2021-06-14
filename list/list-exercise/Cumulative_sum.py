
# Python program to find Cumulative sum of a list


"""
Input : list = [10, 20, 30, 40, 50]
Output : [10, 30, 60, 100, 150]

Input : list = [4, 10, 15, 18, 20]
Output : [4, 14, 29, 47, 67]
"""

def Cumulative_sum(a):
    new_list = []
    sum = 0
    for i in range(0, len(a)):
        sum += a[i]
        new_list.append(sum)
    
    print(new_list)     


if __name__=="__main__":
    list = [10, 20, 30, 40, 50]
    Cumulative_sum(list)   
