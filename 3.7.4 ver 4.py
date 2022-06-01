with open('input.txt', 'r', encoding='UTF-8') as file:
    n = int(file.readline())
    instruction = [file.readline().split() for i in range(n)]
step: int
move = {'север': lambda step: (x, y + step),
        'юг': lambda step: (x, y - step),
        'запад': lambda step: (x - step, y),
        'восток': lambda step: (x + step, y)}
x, y = 0, 0
for i in range(n):
    step = int(instruction[i][1])
    direction = instruction[i][0]
    x, y = move[direction](step)
print(x, y)