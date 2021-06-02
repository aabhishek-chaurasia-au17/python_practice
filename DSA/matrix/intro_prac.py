a = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    ]

x = 1

n = len(a)
m = len(a[0])

for i in range(n):
    for j in range(m):
        print(a[i][j], end=" ")
    print()
    
