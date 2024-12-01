#1
try:
    a=int(input())
    b=int(input())
    print(a/b)
except ZeroDivisionError:
    print("Деление на ноль невозможно")
except ValueError:
    print("Некорректные данные")