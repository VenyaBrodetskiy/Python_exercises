f = open('input.txt', 'r')
s = f.read().lower().strip().split()
print(s)
f.close()
massive = set(s)
#d1 = {i: s.count(i) for i in s}
#print(d1)
d = {}
for i in massive:
    d[i] = s.count(i)
print(d)
#print(d1==d)
output = []
for i in d:
    if d[i] == max(d.values()):
        output.append(i)
print(output)
print(min(output), d[min(output)])