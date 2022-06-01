with open('input.txt', 'r', encoding='UTF-8') as file:
    n = int(file.readline())
    instruction = [file.readline().split() for i in range(n)]

class Turtle:
    start_x = 0
    start_y = 0

    def __init__(self, x = start_x, y = start_y):
        self.x = x
        self.y = y

    def move(self, direction, step):
        if direction == 'север': self.y += step
        elif direction == 'юг': self.y -= step
        elif direction == 'восток': self.x += step
        elif direction == 'запад': self.x -= step

turtle = Turtle()
for i in range(n):
    step = int(instruction[i][1])
    direction = instruction[i][0]
    turtle.move(direction, step)
print(turtle.x, turtle.y)
