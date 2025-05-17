import random

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
		#a = 2
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


n = int(input("Введіть число: "))
k = 5

print(millerRabine(n, k))

