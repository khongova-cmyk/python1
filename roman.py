try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    result = num1 / num2

except ValueError:
    print("Ошибка: Введено нечисловое значение!")

except ZeroDivisionError:
    print("Ошибка: Деление на ноль невозможно!")

else:
    print(f"Результат деления: {result}")

finally:
    print("Программа завершила работу.")