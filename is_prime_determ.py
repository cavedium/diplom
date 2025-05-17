#Якщо n велике непарне число, то перевіряється його подільність
#на всі непарні числа в діапазоні від 3 до корня з n

import math

def is_prime(n):
	if n <= 2:
		return n == 2
	if n % 2 == 0:
		return False
	return all(n % d for d in range(3, math.isqrt(n) + 1, 2))

n = int(input("Enter a number: "))
prime = is_prime(n)
#print(prime)

if prime == False:
	while is_prime(n) == False:
		n = n + 1
		if is_prime(n) == True:
			break
	print("The number is not prime!")
	print(f"The nearest prime number: {n}")
else:
	print(f"The number is prime!")
