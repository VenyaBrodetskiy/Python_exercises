n = 1
a = [[0 for i in range(n)] for j in range(n)]
count = 1
for j in range((n + 1)//2):
    a[0 + j][0 + j] = count
    for i in range(j, n - 1 - j):
        a[j][i] = count
        count += 1
    for i in range(j, n - 1 - j):
        a[i][-1 - j] = count
        count += 1
    for i in range(n - 1 - j, j, -1):
        a[-1 - j][i - n] = count
        count += 1
    for i in range(n - 1 - j, j, -1):
        a[i - n][j] = count
        count += 1
for i in range(n):
    for j in range(n):
        print(a[i][j], end = ' ')
    print()