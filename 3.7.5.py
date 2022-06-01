from statistics import mean
grades = [[0] for i in range(11)]
with open('input.tsv', 'r', encoding='UTF-8') as file:
    data = file.read().split('\n')
print(data)
for i in range(len(data)):
    grade, name, h = data[i].split('\t')
    grade, h = int(grade), int(h)
    grades[grade - 1].append(h)
print(grades)
for i in range(len(grades)):
    if grades[i] == [0]:
        print(f'{i + 1} -')
    else:
        print(f'{i + 1} {mean(grades[i][1:])}')
