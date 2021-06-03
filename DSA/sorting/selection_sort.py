# Selection Sorting 

def selection_sort(A):
    n = len(A)
    for i in range(n):
        min_element = A[i]
        min_ele_indx = i
        for index in range(i,len(A)):
            if A[index] < min_element:
                min_element = A[index]
                min_ele_indx = index
            A[i],A[min_ele_indx] = A[min_ele_indx],A[i]
    
    return A

if __name__=="__main__":
    
    A = [4,8,7,2,6,3,5,1]

    print(selection_sort(A)) 