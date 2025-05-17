import multiplicative_inversion

def is_generator(a, b):
    temp = 1
    for i in range(1, b-2):
        temp = (temp * a) % b
        if temp == 1:
            return False
    temp = (temp * a) % b
    return True

""" def find_next_generator(current, p):
    g = current + 1
    while g < p:
        if is_generator(g, p):
            return g
        g += 1
    return None  # Якщо не знайдено (наприклад, перевищено p) """

""" def find_next_generator(current, p, step):
	step = step + 1
	for i in range(step, p):
		if multiplicative_inversion.NSD(i, p-1) == 1:
			temp = current ** i
			temp = temp % p
			return temp, step
		else:
			break """

def find_next_generator(p, current, prime_factors):
	phi = int(p - 1)
	for g in range(current, p):
		is_generator = True
		for q in prime_factors:
			if pow(g, phi // q, p) == 1:
				is_generator = False
				break
		if is_generator:
			return g
	return None