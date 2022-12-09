from random import randint

def list_unique_numbers() -> list[int]:
    get_numbers = [randint(-10, 10) for _ in range(15)]
    a = set(get_numbers)
    while len(a) < 15:
        a = list(a)
        a.append(randint(-10, 10))
        a = set(a)
    return list(a)


print(list_unique_numbers())
# Вторая проверка не требуется тк цикл в функции работает на постусловии 15 уникальных чисел
