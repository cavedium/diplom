import random
import math
import time

def generate_random_number(length):
    first_digit = str(random.randint(1, 9))
    other_digits = ''.join(str(random.randint(0, 9)) for i in range(length - 1))
    return first_digit + other_digits

def is_prime(n):
	if n <= 2:
		return n == 2
	if n % 2 == 0:
		return False
	return all (n % d for d in range(3, math.isqrt(n) + 1, 2))

#Якщо вводити довжину числа
length = int(input("Введіть довжину числа: "))

#Якщо вводити кількість біт
#bit_length = int(input("Введіть кількість біт: "))
#max_number = 2 ** bit_length - 1
#length = len(str(max_number))

start = time.perf_counter()

if length <= 0:
	print("Довжина має бути більше 0!")
else:
	random_number = int(generate_random_number(length))
	print(f"Згенероване число: {random_number}")
	prime = is_prime(random_number)
	if prime == False:
		while is_prime(random_number) == False:
			random_number = random_number + 1
			if is_prime(random_number) == True:
				break
		print("The number is not prime!")
		print(f"The nearest prime number: {random_number}")
	else:
		print(f"The number is prime!")

end = time.perf_counter()
print(f"Время выполнения: {end - start:.4f} секунд")