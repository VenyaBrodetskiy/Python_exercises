n = 50
i = 1
k = 1
l = 0
res = ''
while l != n:
    while (i <= k) and (l != n):
        res = res + str(k) + ' '
        l += 1
        i += 1
    k += 1
    i = 1
print(res)
