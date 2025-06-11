#Ця функція генерує псевдовипадкове число заданої довжини, 
# уникаючи нуля на початку (щоб воно було повноцінним числом). 
# Якщо довжина менше або дорівнює нулю, виконання не продовжується.

import random

def generate_random_number(length):
    # Генеруємо першу цифру (від 1 до 9, щоб не було нуля на початку)
    first_digit = str(random.randint(1, 9))
    
    # Генеруємо решту цифр (від 0 до 9)
    other_digits = ''.join(str(random.randint(0, 9)) for i in range(length - 1))
    
    return first_digit + other_digits

#Якщо вводити довжину числа
#length = int(input("Введіть довжину числа: "))

#Якщо вводити кількість біт
bit_length = int(input("Введіть кількість біт: "))
max_number = 2 ** bit_length - 1
length = len(str(max_number))

if length <= 0:
	print("Довжина має бути більше 0!")
else:
	random_number = generate_random_number(length)
	print(f"Згенероване число: {random_number}")