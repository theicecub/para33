try:
    numbers = [1,2,3]
    print(numbers[5])
except Exception as e:
    print("Обращение к неверному индексу")

try:
    a = 10
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("Деление на ноль")

try:
    a="123фы"
    print(int(a))
except ValueError:
    print("Ошибка конвертации")
else:
    print("Ошибок не было!")
finally:
    print("Код выполнился")



#Генерация ошибок

age =-5

if age < 0:
    raise ValueError("Возраст не может быть отрицательным")