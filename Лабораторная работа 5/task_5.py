from random import sample

def get_random_password(n=8) -> str:
    base = 'ABCDEFGHJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    return "".join(sample(base, n))


print(get_random_password())
print(get_random_password(5)) # доп. проверка
