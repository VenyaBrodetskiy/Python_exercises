a = 5.0
b = 0
c = str('*')

if c == "mod":
    if b != 0: print(a%b)
    else: print("Деление на 0!")
elif c == 'pow': print(a**b)
elif c == 'div':
    if b != 0: print(a//b)
    else: print("Деление на 0!")
elif c == '/':
    if b != 0: print(a/b)
    else: print("Деление на 0!")
elif c == '+': print(a+b)
elif c == '-': print(a-b)
elif c == '*': print(a*b)


operations = {
      "+": lambda x, y: x + y,
      "-": lambda x, y: x - y,
      "/": lambda x, y: x / y,
      "*": lambda x, y: x * y,
      "mod": lambda x, y: x % y,
      "pow": lambda x, y: x ** y,
      "div": lambda x, y: x // y
}
print(type(operations))
x, y = 5, 2
operation = '+'

if operation in ["mod", "div", "/"] and y == 0:
    print("Деление на 0!")
else:
    print(operations[operation](x, y))