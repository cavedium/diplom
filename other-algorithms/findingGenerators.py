def generators(a, b):
    temp = 1
    for i in range(1, b-2):
        temp = (temp * a) % b
        if temp == 1:
            return False
    temp = (temp * a) % b
    return True

n = int(input("Enter a positive integer number: "))
k = 0

for g in range(2, n):
    if generators(g, n):
        k = k + 1
        print(f"{g} is a generator of", n)
print(f"{k} generators")

""" from math import gcd

# Функція Ейлера (кількість чисел менших за n і взаємно простих з n)
def euler_phi(n):
    result = 0
    for i in range(1, n + 1):
        if gcd(i, n) == 1:
            result += 1
    return result

# Функція для знаходження кількості генераторів простого числа p
def count_generators(p):
    if not is_prime(p):
        return 0  # генератори шукають лише для простих
    return euler_phi(p - 1)

# Перевірка на простоту (простий варіант)
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 🔍 Приклад
p = 475417
print(f"Кількість генераторів для {p}: {count_generators(p)}")
 """