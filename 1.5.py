a = 8
b = 2
c = 14

m = [a, b, c]
print(max(m))
m.remove(max(m))
print(min(m))
m.remove(min(m))
print(m[0])