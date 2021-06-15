
# Python program to add two Matrices
"""
Input :
 X= [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
 
Output :
 result= [[10,10,10],
         [10,10,10],
         [10,10,10]]
"""
print("------------try-------------")

def add_two_matrix(x,y,result):
    
    for i in range(len(x)):
        for j in range(len(x[0])):
            result[i][j] = x[i][j] + y[i][j]


    for a in result:
        print(a)         
            

if __name__=="__main__":
    x = [[1,2,3],
        [4,5,6],
        [7,8,9]]
 
    y = [[9,8,7],
        [6,5,4],
        [3,2,1]]

    result = [[0,0,0],
             [0,0,0],
             [0,0,0]]    

    add_two_matrix(x,y,result)




 
