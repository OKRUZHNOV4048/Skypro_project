def divide(x, y):
    return int(x / y)


print(divide(20, 10))

assert divide(20, 10) == 2

if divide(20, 10) != 2:
    raise Exception("Ошибка!")
