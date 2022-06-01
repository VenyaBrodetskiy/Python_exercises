with open('input.txt', 'r') as file:
    str1, str2, ex1, ex2 = file.read().split('\n')

s1, s2 = list(str1), list(str2)
d1 = dict(zip(s1, s2))
d2 = dict(zip(s2, s1))
out1, out2 = '', ''
for i in ex1:
    out1 += d1[i]
print(out1)
for i in ex2:
    out2 += d2[i]
print(out2)

