s = [['9', '5', '3'], ['0', '7', '-1'], ['-5', '2', '9'], ['0', '0', '0'], ['end']]
s.remove(['end'])
y = len(s)
x = len(s[0])
output = []
for i in range(y):
    for j in range(x):
        ans = int(s[i - 1][j]) + int(s[i + 1 - y][j]) + int(s[i][j - 1]) + int(s[i][j + 1 - x])
        print(ans, end = ' ')
    print()

