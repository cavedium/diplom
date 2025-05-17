import random
import math

def generate_random_number(length):
    first_digit = str(random.randint(1, 9))
    other_digits = ''.join(str(random.randint(0, 9)) for i in range(length - 1))
    return first_digit + other_digits

def millerRabine(n, k):
	if n < 2:
		return False
	if n == 2 | n == 3:
		return True
	if n % 2 == 0:
		return False
	#n - 1 у вигляді 2^s * t
	s = 0
	t = n - 1
	while t % 2 == 0:
		t //= 2
		s += 1
	#Цикл А: повторити k разів
	for _ in range(k):
		a = random.randint(2, n - 2)
		x = pow(a, t, n)
		if x == 1 or x == n - 1:
			continue
			# Цикл В: повторити s - 1 раз
		for i in range(s - 1):
			x = pow(x, 2, n)
			if x == 1:
				return False
			if x == n - 1:
				break
		else:
			return False
	return True # Число є ймовірно простим

def get_number(bit_length):
	max_number = 2 ** bit_length - 1
	length = len(str(max_number))
	if length <= 0:
		return 0
	else:
		random_number = int(generate_random_number(length))
		#print(f"Згенероване число: {random_number}")
		prime = millerRabine(random_number, 5)
		if prime == False:
			while millerRabine(random_number, 5) == False:
				random_number = random_number + 1
				if millerRabine(random_number, 5) == True:
					return random_number
			#print("The number is not prime!")
			#print(f"The nearest prime number: {random_number}")
		else:
			return random_number
			#print(f"The number is prime!")
