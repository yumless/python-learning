x = int(input("Введите первое число - "))
c = input("введите операцию - ")
y = int(input("Введите второе число - "))
if c == "+":
    r = x + y
elif c == "-":
    r = x - y
elif c == "*":
    r = x * y
elif c == "/":
    r = x / y
print(f"Результат {r}")