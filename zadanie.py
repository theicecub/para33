#1
try:
    a=int(input())
    b=int(input())
    c = a/b
except (ZeroDivisionError, ValueError):
    print("Деление на ноль или неправильная конвертация типов")
else:
    print(c)

#2
try:
    isEven=False
    num=int(input())
    if(num % 2 == 0):
        isEven = True
except ValueError:
    print("Неправильная конвертация типов")
else:
    if(isEven == True):
        print("Число четное")
    else:
        print("Число нечетное")