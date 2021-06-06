"""
sample input
3
1 2 3
sample output
2
# Print count of sub array which have odd sum
Sub array are :
[1]
[1,2]
[1,2,3]
[2]
[2,3]
[3]

sub array that have odd sum are : [1,2,3] and [2],
so the answer is - >  2
"""

n = 3 # user_input
a = [1,2,3]
count = 0
for i in range(n):
    res = []
    for j in range(i,n):
        res.append(a[j])
        if sum(res)%2!=0:
            count +=1
print(count)
