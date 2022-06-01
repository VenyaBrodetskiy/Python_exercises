f = open('big data.txt', 'r')
n, r = f.readline().strip().split()
n = int(n)
r = int(r)
print('N и R =', n, r)
sensor = [int(f.readline().strip()) for i in range(n)]
print('Список датчиков', sensor)
f.close()
# заполняем список квадратов расстояний между точками
# список симметричный (как бином Ньютона), поэтому делаем только половину списка
l = []
for i in range(n//2 + 1):
    #l.append((i * r)  2)
    l.append(i ** 2)
# для примера из задачи получается [0, 2, 4, 6] вместо [0, 2, 4, 6, 4, 2]
print('Список расстояний между точками', l)
# считаем энергию для каждого датчика
energy = [0] * n
for i in range(n):
    for j in range(n//2 + 1):
        energy[i] += (sensor[i - j] + sensor[i - n + j]) * l[j]
    print(energy[i])
    print('Progress:', round(i / n * 100, 3), '%')
# вывод индекса минимального элемента
print('Energy list:', energy)
print('Answer:', energy.index(min(energy)) + 1)