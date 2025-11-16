import time
import os

def topla(param1: int, param2: int):
	return param1 + param2

if __name__ == "main":

	print("Merhaba, terminal için hazırlanmış olan yazı tabanlı, ve nedense sadece toplama işlemi yapan hesap makinesine hoş geldiniz.")
	time.sleep(0.25)
	print("Lütfen toplayacağınız iki sayıyı girin:")

	toplanacak1 = int(input(f"Sayı 1: "))
	toplanacak2 = int(input(f"Sayı 2: "))

	print(f"Toplamınız: {topla(toplanacak1, toplanacak2)}")
