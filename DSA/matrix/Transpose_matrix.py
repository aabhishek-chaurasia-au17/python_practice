# Transpose a matrix in Single line in Python
"""
input :- m = [[1,2],[3,4],[5,6]]

out put :-  [1, 2]
            [3, 4]
            [5, 6]

        [1, 3, 5]
        [2, 4, 6]
"""

m = [[1,2],[3,4],[5,6]]

for row in m:
    print(row)

rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

for row in rez:
    print(row)

