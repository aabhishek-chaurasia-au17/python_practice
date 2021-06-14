
arry = [
        [4,5,6],
        [9,8,7],
        [8,5,2]
        ]

n = 3
m = 3

row = 0
col = 0

while row < n and col < m:
    print(arry[row][col])
    row += 1
    col += 1

# for i in range(min(n,m)):
#     print(arry[i][i]  )