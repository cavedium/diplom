#Порядок групи + елементи групи
from math import gcd

def multiplicative_group(n):
    group = [x for x in range(1, n) if gcd(x, n) == 1]
    return group

n = 475417
group = multiplicative_group(n)
print(f"Кількість елементів в групі Z_{n}^*:", len(group))
print("Перші 30 елементів групи:", group[:30])

#Порядок групи
from sympy import totient

print(totient(n))