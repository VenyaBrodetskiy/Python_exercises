import random

for i in range(10):
    a = random.randint(0, 1000)
    if (a % 10 == 1) and (a % 100 != 11):
        print(a, ' программист')
    elif (2 <= a % 10 <= 4) and not (12 <= a % 100 <= 14):
        print(a, ' программиста')
    else:
        print(a, ' программистов')
