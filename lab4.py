def z1():
    a = int(input("Введите число для деления его на 3: "))
    ostat = a % 3
    if ostat == 0:
        print("Число делится на 3")
    else:
        print("Число не делится на 3")
    return ostat
print(z1())

def z2():
    try:
        a = int(input("Введите число для деления его на 100: "))
        ostat = 100 / a
    except ValueError:
        print("Введите число")

    except ZeroDivisionError:
        print("Деление на ноль")
    return ostat
print(z2())

def z3():
    x, y, z = map(int, date.split("."))
    if x * y == z % 100:
        return True
    else:
        return False
date = input("Введите дату: ")
if z3():
    print(f"{date} - магическая дата")
else:
    print(f"{date} - немагическая дата")