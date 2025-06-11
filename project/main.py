import customtkinter as CTk
import key
import multiplicative_inversion
import prime_factors
import nextGenerators

class App(CTk.CTk):
	def __init__(self):
		super().__init__()

		self.geometry("960x700")
		self.title("ДОСЛІДЖЕННЯ ВЛАСТИВОСТЕЙ МУЛЬТИПЛІКАТИВНОЇ ГРУПИ КІЛЬЦЯ ЛИШКІВ")
		self.resizable(False, False)
		#* ПУНКТ №1
		self.key_generator_label = CTk.CTkLabel(master=self, text="1) Генератор простого числа (Перевірка на простоту)", font=("Times New Roman", 16))
		self.key_generator_label.grid(row=0, column=0, padx=(20, 0), pady=(0, 5), sticky="nw")
		
		self.key_generator_frame = CTk.CTkFrame(master=self, fg_color="transparent")
		self.key_generator_frame.grid(row=1, column=0, padx=(20, 20), sticky="nsew")
		
		self.entry_key = CTk.CTkEntry(master=self.key_generator_frame, width = 600, placeholder_text="Введіть просте число або згенеруйте нове")
		self.entry_key.grid(row=0, column=0, padx=(0, 10))

		self.btn_generate = CTk.CTkButton(master=self.key_generator_frame, text="Generate", width = 100,
									command=self.set_key)
		self.btn_generate.grid(row=0, column=1, padx=(0, 10))

		self.btn_is_prime = CTk.CTkButton(master=self.key_generator_frame, text="Is Prime?", width = 100,
									command=self.is_prime)
		self.btn_is_prime.grid(row=0, column=2, padx=(0, 10))
		
		self.is_prime_label = CTk.CTkLabel(master=self.key_generator_frame, text="")
		self.is_prime_label.grid(row=0, column = 3)
		
		self.settings_frame = CTk.CTkFrame(master=self)
		self.settings_frame.grid(row=2, column=0, padx=(20, 20), pady=(10, 10), sticky="nsew")
		
		self.key_length_slider = CTk.CTkSlider(master=self.settings_frame, from_= 1 , to = 1024, number_of_steps = 1024, width=800,
									command=self.slider_event)
		self.key_length_slider.grid(row=1, column=0, columnspan=3, padx=(10, 0), pady=(20, 20), sticky="ew")
		
		self.key_length_entry = CTk.CTkEntry(master=self.settings_frame, width=75, placeholder_text="К-сть біт")
		self.key_length_entry.grid(row=1, column=3, padx=(20, 10), sticky="we")
		self.key_length_entry.bind("<KeyRelease>", self.slider_entry_event)
		#* ПУНКТ №2
		self.multiplicative_inversion_label = CTk.CTkLabel(master=self, text="2) Знаходження мультиплікативної інверсії числа", font=("Times New Roman", 16))
		self.multiplicative_inversion_label.grid(row=3, column=0, padx=(20, 0), pady=(0, 5), sticky="nw")
		
		self.multiplicative_inversion_frame = CTk.CTkFrame(master=self)
		self.multiplicative_inversion_frame.grid(row=4, column=0, padx=(20, 20), pady=(0, 10), sticky="nsew")
		
		self.element_of_group_entry = CTk.CTkEntry(master=self.multiplicative_inversion_frame, width=150, placeholder_text="Введіть елемент групи")
		self.element_of_group_entry.grid(row = 0, column=0, padx=(10, 10), pady=(10, 0), sticky="nw")
		self.element_of_group_label = CTk.CTkLabel(master=self.multiplicative_inversion_frame, text="ЕЛЕМЕНТ ГРУПИ\nвід 1 до модуля групи", font=("Calibri", 12))
		self.element_of_group_label.grid(row=1, column=0, padx=(20, 0), sticky="nw")
		
		#self.element_of_group_condition_label = CTk.CTkLabel(master=self.multiplicative_inversion_frame, text="який, буде помножений на", font=("Times New Roman", 16))
		self.element_of_group_condition_label = CTk.CTkLabel(master=self.multiplicative_inversion_frame, text="помножений на", font=("Times New Roman", 16))
		self.element_of_group_condition_label.grid(row=0, column=1, padx=(0, 0), pady=(10, 0))

		self.element_of_group_inversion_entry = CTk.CTkEntry(master=self.multiplicative_inversion_frame, width=180, placeholder_text="Мультиплікативну інверсію")
		self.element_of_group_inversion_entry.grid(row=0, column=2, padx=(0, 5), pady=(10, 0))
		self.element_of_group_inver_label = CTk.CTkLabel(master=self.multiplicative_inversion_frame, text="МУЛЬТИПЛІКАТИВНА ІНВЕРСІЯ", font=("Calibri", 12))
		self.element_of_group_inver_label.grid(row=1, column=2, padx=(50, 0), sticky="nw")
		
		self.element_of_group_inversion_label = CTk.CTkLabel(master=self.multiplicative_inversion_frame, text="по модулю групи дорівнює", font=("Times New Roman", 16))
		self.element_of_group_inversion_label.grid(row=0, column=3, pady=(10, 0), padx=(0, 10))
	
		self.nsd_entry = CTk.CTkEntry(master=self.multiplicative_inversion_frame, width=150, placeholder_text="якщо '1', то все вірно")
		self.nsd_entry.grid(row=0, column=4, padx=(0, 10), pady=(10, 0))
		self.nsd_entry_label = CTk.CTkLabel(master=self.multiplicative_inversion_frame, text="якщо '1, то все вірно'", font=("Calibri", 12))
		self.nsd_entry_label.grid(row=1, column=4, padx=(20, 0), sticky="nw")

		#self.formula_label = CTk.CTkLabel(master=self.multiplicative_inversion_frame, text="")
		#self.formula_label.grid(row=2, column=0, pady=(10, 0))

		self.multiplicative_inversion_btn = CTk.CTkButton(master=self.multiplicative_inversion_frame, text="Знайти мультиплікативну інверсію", width=150,
													command=self.multiplicative_inversion)
		self.multiplicative_inversion_btn.grid(row=3, column=2, padx=(40, 0), pady=(5, 10))

		self.formula_label = CTk.CTkLabel(master=self, text="")
		self.formula_label.grid(row=5, column=0)
		#* ПУНКТ №3
		self.group_factorisation_label = CTk.CTkLabel(master=self, text="3) Факторизація порядку групи", font=("Times New Roman", 16))
		self.group_factorisation_label.grid(row=6, column=0, padx=(20, 0), pady=(0, 5), sticky="nw")
		
		self.group_factorisation_frame = CTk.CTkFrame(master=self)
		self.group_factorisation_frame.grid(row=7, column=0, padx=(20, 20), pady=(0, 10), sticky="nsew")
		

		self.ord_of_group_entry_label = CTk.CTkLabel(master=self.group_factorisation_frame, text="Порядок групи:")
		self.ord_of_group_entry_label.grid(row=0, column=0, padx=(15, 0), pady=(10, 10), sticky="nw")
		self.ord_of_group_entry = CTk.CTkEntry(master=self.group_factorisation_frame, width=770, placeholder_text="Порядок групи")
		self.ord_of_group_entry.grid(row=0, column=0, padx=(130, 0), pady=(10, 10), sticky="nw")
		
		self.count_of_generators_entry_label = CTk.CTkLabel(master=self.group_factorisation_frame, text="К-сть генераторів:")
		self.count_of_generators_entry_label.grid(row=1, column=0, padx=(15, 0), sticky="nw")
		self.count_of_generators_entry = CTk.CTkEntry(master=self.group_factorisation_frame, width=770, placeholder_text="Кількість генераторів")
		self.count_of_generators_entry.grid(row=1, column=0, padx=(130, 0), sticky="nw")
		
		self.prime_factors_textbox = CTk.CTkTextbox(master=self.group_factorisation_frame, width=150, height=125, wrap="word")
		self.prime_factors_textbox.grid(row=2, column=0, padx=(15, 0), pady=(10, 10), sticky="nw")
		
		self.group_factorisation_btn = CTk.CTkButton(master=self.group_factorisation_frame, text="Факторизувати", width=150,
										command=self.insert_prime_factors)
		self.group_factorisation_btn.grid(row=3, column=0, padx=(15, 0), sticky="nw")
		
		self.ord_of_element_frame = CTk.CTkFrame(master=self.group_factorisation_frame, width=100, height=100)
		self.ord_of_element_frame.grid(row=2, padx=(200, 0), pady=(10, 0), sticky="nsew")
		#* ПУНКТ №4
		self.ord_of_element_label = CTk.CTkLabel(master=self.ord_of_element_frame, text="4) Визначити порядок елемента", font=("Times New Roman", 16))
		self.ord_of_element_label.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="nw")

		self.entry_ord_element_of_group = CTk.CTkEntry(master=self.ord_of_element_frame, width=150, placeholder_text="Введіть елемент групи")
		self.entry_ord_element_of_group.grid(row=1, column=0, padx=(10, 10), pady=(10, 0), sticky="nw")
		self.ord_element_of_group_label = CTk.CTkLabel(master=self.ord_of_element_frame, text="від 1 до модуля групи", font=("Calibri", 12))
		self.ord_element_of_group_label.grid(row=2, column=0, padx=(20, 0), sticky="nw")
		
		self.ord_of_element_entry = CTk.CTkEntry(master=self.ord_of_element_frame, width=150, placeholder_text="Порядок елемента")
		self.ord_of_element_entry.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky="nw")

		self.ord_of_element_btn = CTk.CTkButton(master=self.ord_of_element_frame, text="Визначити порядок елемента", width = 100,
										command=self.ord_the_element)
		self.ord_of_element_btn.grid(row=4, column=0, padx=(0, 10), pady=(10, 10))

		self.ord_the_element_label = CTk.CTkLabel(master=self.ord_of_element_frame, text="", width=175)
		self.ord_the_element_label.grid(row=4, column=1)
		#* ПУНКТ №5
		self.next_generator_label = CTk.CTkLabel(master=self.ord_of_element_frame, text="5) Вичислення наступного генератора", font=("Times New Roman", 16),)
		self.next_generator_label.grid(row=0, column=4, padx=(0, 0), pady=(0, 0))
		
		self.next_generator_entry = CTk.CTkEntry(master=self.ord_of_element_frame, width=200, placeholder_text="Значення генератора")
		self.next_generator_entry.grid(row=1, column=4)
		
		self.next_generator_btn = CTk.CTkButton(master=self.ord_of_element_frame, text="Вичислити наступний генератор", width=200,
										command=self.next_generator)
		self.next_generator_btn.grid(row=2, column=4, pady=(10, 0))
		
		self.memory_entry = CTk.CTkEntry(master=self.ord_of_element_frame, placeholder_text="Память")
		self.memory_entry.grid_forget()

	def next_generator(self): #TODO НАПИСАТИ ФУНКЦІЮ ПОШУКУ НАСТУПНОГО ГЕНЕРАТОРА
		try:
			if self.count_of_generators_entry.get() == "0":
				self.show_error("КІЛЬКІСТЬ ГЕНЕРАТОРІВ ДОРІВНЮЄ 0!")
			else:
				if self.ord_of_element_entry.get() == "":
					self.show_error("ВВЕДІТЬ ЕЛЕМЕНТ ГРУПИ В ПУНКТІ 4!")
				q_list = []
				for p, e in prime_factors.prime_factors(int(int(self.ord_of_group_entry.get()))):
						q_list.append(p)
				self.next_generator_entry.delete(0, "end")
				self.next_generator_entry.insert(0, nextGenerators.find_next_generator(int(self.entry_key.get()), int(self.memory_entry.get()), q_list))
				self.memory_entry.delete(0, "end")
				self.memory_entry.insert(0, (int(self.next_generator_entry.get()) + 1))
			#current = int(self.entry_ord_element_of_group.get())
			#next_gen, step = nextGenerators.find_next_generator(current, int(self.entry_key.get()), int(self.step_entry.get()))
			#if next_gen:
			#	self.next_generator_entry.delete(0, "end")
			#	self.step_entry.delete(0, "end")
			#	self.next_generator_entry.insert(0, int(next_gen))
			#	self.step_entry.insert(0, int(step))

			#if multiplicative_inversion.NSD(step, mod) == 1:
			#	step = step + 1
			#	temp = current ** step
			#	temp = temp % (int(self.entry_key.get()))
			#	self.next_generator_entry.insert(0, int(temp))
			#else:
			#	self.next_generator_entry.delete(0, "end")
			#	self.next_generator_entry.insert(0, "Відсутній")
		except ValueError:
			self.next_generator_entry.delete(0, "end")
			self.next_generator_entry.insert(0, "Помилка")

	def ord_the_element(self):
		if self.entry_ord_element_of_group.get() == "":
			self.ord_the_element_label.configure(text="ВВЕДІТЬ ЕЛЕМЕНТ ГРУПИ")
			self.show_error("ВВЕДІТЬ ЕЛЕМЕНТ ГРУПИ В ПУНКТІ 4!")
		else:
			if nextGenerators.is_generator(int(self.entry_ord_element_of_group.get()), int(self.entry_key.get())) == True:
				if self.count_of_generators_entry.get() == "0":
					self.ord_the_element_label.configure(text="Генератори відсутні")
				else:
					self.ord_the_element_label.configure(text="Генератор групи")
				self.memory_entry.delete(0, "end")
				self.memory_entry.insert(0, self.entry_ord_element_of_group.get())
			else:
				if self.count_of_generators_entry.get() == "0":
					self.ord_the_element_label.configure(text="Генератори відсутні")
				else:
					self.ord_the_element_label.configure(text="Не Генератор групи")
			self.ord_of_element_entry.delete(0, "end")
			self.ord_of_element_entry.insert(0, int(prime_factors.ord_of_element(int(self.entry_ord_element_of_group.get()), int(self.entry_key.get()))))

	def insert_prime_factors(self):
		if self.entry_key.get() == "":
			#self.entry_key.configure(placeholder_text_color="red", border_color="red")
			self.show_error("ВВЕДІТЬ ЧИСЛО ДЛЯ ПЕРЕВІРКИ В ПУНКТІ 1!")
		else:
			self.ord_of_group_entry.delete(0, "end")
			self.count_of_generators_entry.delete(0, "end")
			self.prime_factors_textbox.delete("0.0", "end")
			self.ord_of_group_entry.insert(0, int(prime_factors.ord_of_group(int(self.entry_key.get()))))
			self.count_of_generators_entry.insert(0, int(prime_factors.count_generators(int(self.entry_key.get()))))
			for p, e in prime_factors.prime_factors(int(int(self.ord_of_group_entry.get()))):
					self.prime_factors_textbox.insert("end", f"{p} в степені {e}\n")

	def multiplicative_inversion(self):
		if self.element_of_group_entry.get() == "":
			self.show_error("ВВЕДІТЬ ЕЛЕМЕНТ ГРУПИ\nАБО\nЧИСЛО ДЛЯ ПЕРЕВІРКИ В ПУНКТІ 1!")
			#if self.entry_key.get() == "":
				#self.entry_key.configure(placeholder_text_color="red", border_color="red")
				#self.show_error("ВВЕДІТЬ ЧИСЛО ДЛЯ ПЕРЕВІРКИ!")
		else:
			if int(self.element_of_group_entry.get()) > 0:
				self.element_of_group_entry.configure(placeholder_text_color="#FFFFFF", border_color="#565B5E")
				self.entry_key.configure(placeholder_text_color="#FFFFFF", border_color="#565B5E")
				if multiplicative_inversion.invertedElement(int(self.element_of_group_entry.get()), int(self.entry_key.get())) == False:
					self.element_of_group_inversion_entry.delete(0, "end")
					self.element_of_group_inversion_entry.insert(0, int(multiplicative_inversion.invertedElement(int(self.element_of_group_entry.get()), int(self.entry_key.get()))))
					self.nsd_entry.delete(0, "end")
					self.nsd_entry.insert(0, int(multiplicative_inversion.NSD(int(self.element_of_group_entry.get()), int(self.entry_key.get()))))
					#self.element_of_group_inversion_entry.configure(placeholder_text="Не є елементом групи")
					self.formula_label.configure(text=f"{self.element_of_group_entry.get()} * {self.element_of_group_inversion_entry.get()}mod{self.entry_key.get()} = {self.nsd_entry.get()}\nНЕ Є ЕЛЕМЕНТОМ ГРУПИ")
				else:
					self.element_of_group_inversion_entry.delete(0, "end")
					self.element_of_group_inversion_entry.insert(0, int(multiplicative_inversion.invertedElement(int(self.element_of_group_entry.get()), int(self.entry_key.get()))))
					self.nsd_entry.delete(0, "end")
					self.nsd_entry.insert(0, int(multiplicative_inversion.NSD(int(self.element_of_group_entry.get()), int(self.entry_key.get()))))
					self.formula_label.configure(text=f"{self.element_of_group_entry.get()} * {self.element_of_group_inversion_entry.get()}mod{self.entry_key.get()} = {self.nsd_entry.get()}\nЄ ЕЛЕМЕНТОМ ГРУПИ")
			else:
				self.show_error("ЕЛЕМЕНТ НЕ МОЖЕ БУТИ ВІД'ЄМНИМ\nВВЕДІТЬ ЕЛЕМЕНТ ВІД 1 ДО МОДУЛЯ ГРУПИ")

	def slider_event(self, value):
		self.key_length_entry.delete(0, "end")
		self.key_length_entry.insert(0, int(value))
	
	def slider_entry_event(self, event):
		try:
			value = int(self.key_length_entry.get())
			self.key_length_slider.set(value)
		except ValueError:
			pass

	def is_prime(self):
		if self.entry_key.get() == "":
			#self.is_prime_label.configure(text="ВВЕДІТЬ ЧИСЛО")
			self.show_error("ВВЕДІТЬ ЧИСЛО ДЛЯ ПЕРЕВІРКИ!")
		else:
			if key.millerRabine(int(self.entry_key.get()), 5) == True:
				self.is_prime_label.configure(text="Просте")
			else:
				self.is_prime_label.configure(text="Не просте")

	def set_key(self):
		if self.key_length_entry.get() == "":
			#self.entry_key.configure(placeholder_text="ВВЕДІТЬ КІЛЬКІСТЬ БІТ!!!")
			self.show_error("ВВЕДІТЬ КІЛЬКІСТЬ БІТ\nДЛЯ ГЕНЕРАЦІЇ ЧИСЛА!")
		else:
			self.entry_key.delete(0, "end")
			self.entry_key.insert(0, key.get_number(int(self.key_length_entry.get())))

	def show_error(self, text, title="Помилка"):
		error_window = CTk.CTkToplevel(self)
		error_window.title(title)
		error_window.geometry("300x150")
		error_window.grab_set()

		label = CTk.CTkLabel(error_window, text=text, text_color="red")
		label.pack(pady=20)

		close_button = CTk.CTkButton(error_window, text="Закрити", command=error_window.destroy)
		close_button.pack(pady=20)	

if __name__ == "__main__":
	app = App()
	app.mainloop()