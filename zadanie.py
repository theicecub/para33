#1
try:
    a=int(input())
    b=int(input())
    c = a/b
except (ZeroDivisionError, ValueError):
    print("Деление на ноль или неправильная конвертация типов")
else:
    print(c)