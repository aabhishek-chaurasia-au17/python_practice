
a = [1,2,3]
b = []

for i in range(len(a)):
    resulte = []
    for j in range(i, len(a)):
        resulte.append(a[j])
        print(resulte)

    b.append(resulte)