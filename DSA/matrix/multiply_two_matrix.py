# Python program to multiply two matrices

"""
Input : X = [[1, 7, 3],
             [3, 5, 6],
             [6, 8, 9]]
       Y = [[1, 1, 1, 2],
           [6, 7, 3, 0],
           [4, 5, 9, 1]]
 
Output : [55, 65, 49, 5]
         [57, 68, 72, 12]
         [90, 107, 111, 21]

"""

def multiply_two_matrices(x,y,result):

    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                result[i][j] += x[i][k] * y[k][j]

    for a in result:
        print(a)         



if __name__=="__main__":

    x = [[1, 7, 3],
        [3, 5, 6],
        [6, 8, 9]]
    y = [[1, 1, 1, 2],
        [6, 7, 3, 0],
        [4, 5, 9, 1]]

    result = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    
    multiply_two_matrices(x,y,result)

