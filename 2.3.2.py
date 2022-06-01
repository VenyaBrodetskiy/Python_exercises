a = -5
b = 12
n = 0
sum = 0
for i in range(a, b + 1):
    if i % 3 == 0:
       sum += i
       n += 1
print(sum / n)