a = [int(i) for i in input().split()]
""""
b = [0] * len(a)
if len(a) == 1:
    print(a[0])
else:
    b[-1] = a[0] + a[-2]
    for i in range(len(a) - 1):
        b[i] = a[i + 1] + a[i - 1]
    for i in b:
        print(str(i) + ' ', end='')
"""
if len(a) != 1:
    for i in range(len(a)):
        print(a[i - 1] + a[i - len(a) + 1], end= ' ')
else:
    print(a[0])
