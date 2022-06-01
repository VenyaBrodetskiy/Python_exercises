s = [int(i) for i in input().split()]
s.sort()
output = []
for i in s:
    if s.count(i) > 1 and output.count(i) == 0:
        output += [i]
        print(i, end = ' ')