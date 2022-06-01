f = open('input.txt', 'r')
s = f.read()
f.close()
print(s)

output = ''
i = 0
while i < len(s) and s[i].isalpha():
    j = i + 1
    n = ''
    while s[j - len(s)].isdigit():
        n += s[j - len(s)]
        j += 1
    for k in range(int(n)):
        output += s[i]
    i = j
print(output)
f = open('output.txt', 'w')
f.write(output)
f.close()
