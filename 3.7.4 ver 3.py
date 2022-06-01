with open('input.txt', 'r', encoding='UTF-8') as file:
    n = int(file.readline())
    instruction = [file.readline().split() for i in range(n)]
x, y = 0, 0
for i in range(n):
    step = int(instruction[i][1])
    direction = instruction[i][0]
    if direction == 'север': y += step
    elif direction == 'юг': y -= step
    elif direction == 'восток': x += step
    elif direction == 'запад': x -= step
print(x, y)