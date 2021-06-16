# Python | Matrix creation of n*n

n = 4

print(str(n))

res = [list(range(1+n*i, 1+n * (i+1))) for i in range(n)]

print(res)


