def f(x):
    return 2*x
d = {}
x = [5, 12, 9, 20, 12]
for i in set(x):
    d[i] = f(i)
print(d)
for i in x:
    print(d[i])