with open('input.txt', 'r', encoding='utf-8') as file:
    s_buf = file.read().split('\n')
print(s_buf)
s = []
# разбиваю строчки по точке с запятой
for i in s_buf:
    s_temp = i.split(';')
    # меняю оценки на числа
    for j in range(1, len(s_temp)):
        s_temp[j] = int(s_temp[j])
    s.append(s_temp)
print(s)

# вывожу средние оценки по ученикам
output = open('output.txt', 'w', encoding='utf-8')
for i in s:
    average = (i[1] + i[2] + i[3]) / 3
    print(average)
    output.write(str(average)+'\n')

# вывожу средние оценки по предметам
for i in range(1, len(s_temp)):
    summ = 0
    for j in range(len(s)):
        summ += s[j][i]
    print(summ/len(s), end = ' ')
    output.write(str(summ/len(s))+' ')
output.close()


