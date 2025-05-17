from sympy import totient
from math import gcd
import key

def ord_of_group(n):
	return totient(n)

def ord_of_element(a, n):
    if gcd(a, n) != 1:
        return 0
    k = 1
    result = a % n
    while result != 1:
        result = (result * a) % n
        k += 1
    return k

# Функція Ейлера (кількість чисел менших за n і взаємно простих з n)
def euler_phi(n):
    result = 0
    for i in range(1, n + 1):
        if gcd(i, n) == 1:
            result += 1
    return result

# Функція для знаходження кількості генераторів простого числа p
def count_generators(p):
    if not key.millerRabine(p, 5):
        return 0  # генератори шукають лише для простих
    return euler_phi(p - 1)

def prime_factors(n):
    factors = []
    
    # Спочатку ділимо на 2
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    if count > 0:
        factors.append((2, count))

    # Далі пробуємо непарні дільники до √n
    d = 3
    while d * d <= n:
        count = 0
        while n % d == 0:
            n //= d
            count += 1
        if count > 0:
            factors.append((d, count))
        d += 2

    # Якщо залишився простий дільник більше √n
    if n > 1:
        factors.append((n, 1))

    return factors