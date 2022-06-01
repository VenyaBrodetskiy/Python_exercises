with open('input.txt', 'r', encoding='UTF-8') as file:
    n = int(file.readline())
    instruction = [file.readline().split() for i in range(n)]
def north(x, y, step):
    return x, y + step
def south(x, y, step):
    return x, y - step
def west(x, y, step):
    return x - step, y
def east(x, y, step):
    return x + step, y

move = {'север': north,
        'юг': south,
        'запад': west,
        'восток': east}

x, y = 0, 0
for i in range(n):
    step = int(instruction[i][1])
    direction = instruction[i][0]
    x, y = move[direction](x, y, step)
print(x, y)
