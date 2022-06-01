lst = '5 8 2 7 8 8 2 4'
x = 8
s = ''
k = 0
lst = lst.split()
for i in lst:
    if int(i) == x:
        s = s + str(k) + ' '
    k += 1
if s == '':
    print("Отсутствует")
else: print(s)