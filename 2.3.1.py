a = 1
b = 3
c = 2
d = 4
for k in range(c, d + 1):
    print('\t', k, end = '')
print()
for i in range(a, b + 1):
    print(i, end = '\t')
    for j in range(c, d + 1):
        print(j * i, end = '\t')
    print()