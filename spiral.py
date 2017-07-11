n = input()
a = [[0 for i in range(n)] for i in range(n)]
x, y = 0, 0
index = 1
i, j = 0, 0
while a[i][j] == 0:
    a[i][j] = index
    index += 1
    if j + 1 < n and a[i][j+1] == 0 and (i == 0 or a[i-1][j] != 0):
        j += 1
    elif i + 1 < n and a[i+1][j] == 0:
        i += 1
    elif j > 0 and a[i][j-1] == 0:
        j -= 1
    elif i > 0 and a[i-1][j] == 0:
        i -= 1
for i in a:
    for j in i:
        print j,'\t',
    print '\n'
