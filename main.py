
# son = int(input("Istalgan Sonni Kiriting: "))
# son += 1
# for a in range(0, son):
# 	print(a, end=" ")

# print("Kiritilgan Sonning Kvadratiini Qaytaruvchi Dastur. ")
# savol = "Istalgan Son Kiriting "
# savol += "(Dasturni To'xtatish Uchun 'exit' Deb Yozing): "

# while True:
# 	qiymat = input(savol)
# 	if qiymat == 'exit':
# 		break
# 	else:
# 		print(float(qiymat)**2)
# print("Dastur Tugadi")

# sonlar = list(range(1,11))
# for son in sonlar:
# 	if son == 9:
# 		break
# 	print(f"{son} ning kvadrati {son**2} ga teng")

# sonlar = list(range(1,11))
# for son in sonlar:
# 	if son == 10:
# 		continue
# 	print(f"{son} ning kvadrati {son**2} ga teng")

# son = 0
# while son<10:
# 	if son%2!=0:
# 		continue
# 	else:
# 		print(son)

# kitob = ("Yaxshi Ko'rgan Kitobingizni Kiriting: ")
# kitob += "(Dastur To'xtatish Uchun 'stop' Deb Yozing): "
# while True:
# 	savol = input(kitob)
# 	if savol == 'stop':
# 		break
# 	else:
# 		print(f"{savol} sizni yaxshi ko'rgan kitobingiz")

# son = 20
# son2 = 40
# print(20 ** 3)

# sonlar = ("Musbat Son Kiriting: ")
# sonlar += "(Dasturni To'xtatish Uchun 'exit' Deb Yozing) "
# while True:
# 	son = input(sonlar)
# 	if son == 'exit':
# 		break
# 	else:
# 		son1 = int(son)
# 		print(f"{son} ning ildizi {son1**0.5} ga teng")


# print("Yaqin Do'stlaringizni Ro'yxatini Tuzamiz: ")
# ismlar = []
# n = 1
# while True:
# 	savol = f"{n}-Do'stingiz Ismini Kiriting: "
# 	ism = input(savol)
# 	ismlar.append(ism)
# 	takrorlash = input("Yana Ism Qo'shasizmi? (ha/yo'q)")
# 	n += 1
# 	if takrorlash != "ha":
# 		break

# print("Do'stlaringiz Ro'yxati: ")
# for ism in ismlar:
# 	print(ism.title())

# print("Do'stlaringiz Yoshini Saqlaymiz. ")
# dostlar = {}
# ishora = True
# while ishora:
# 	ism = input("Do'stingiz Ismini Kiriting: ")
# 	yosh = input(f"{ism.title()}ning Yoshini Kiriting: ")
# 	dostlar[ism] = int(yosh)

# 	javob = input("Yana Ma'lumot Qo'shasizmi? (ha/yo'q)")
# 	if javob == "yo'q":
# 		ishora = False

# for ism, yosh in dostlar.items():
# 	print(f"{ism.title()} {yosh} yoshda")

# print("Do'stlar Haqida Ma'lumot.")
# dostlar = {}
# ishora = True
# while ishora:
# 	ism = input("Do'stingizni Ismini Kiriting: ")
# 	familya = input("Do'stingizni Familyasini Kiriting: ")
# 	yosh = input("Do'stingizni Yoshini Kiriting: ")
# 	kurs = input("Do'stingiz Nechinchi Sinf: ")
# 	dostlar[ism] = int(yosh)

# 	javob = input("Yana Ma'lumot Qo'shasizmi? (ha/yo'q)")
# 	if javob == "yo'q":
# 		ishora = False
# for ism, yosh in dostlar.items():
# 	print(f"Do'stingiz {ism.title()} {familya} {yosh}yoshda {kurs}-sinfda o'qiydi")

#REMOVE
# cars = ["Lacetti", "Nexia", "Toyota", "Audi", "Malibu", "Nexia", "Lacetti"]
# car = "Lacetti"
# while car in cars:
# 	cars.remove(car)

# print(cars)

#POP
# print("Sinfdoshlar Haqida Ma'lumot")
# sinfdoshlar = {}
# ishora = True
# while ishora:
# 	Familya = input("Familyasini Kiriting: ")
# 	Ism = input("Ismini Kiriting: ")
# 	Yosh = input("Yoshini Kiriting: ")
# 	Sinf = input("Sinfni Kiriting:  ")
# 	sinfdoshlar[Ism] = int(Yosh)

# 	javob = input("Yana Ma'lumot Qo'shasizmi? (ha/yo'q)")
# 	if javob == "ha":
# 		qoshimcha = input("U Sinfdoshingiz Yaxshi O'qiydimi: ")
# 		qoshimcha2 = input("U Sinfdoshingiz Nimaga Qiziqadi: ")
# 	javob = input("Yana Ma'lumot Qo'shasizmi? (ha/yo'q)")
# 	if javob == "yo'q":
# 		ishora = False
# for Ism, Yosh in sinfdoshlar.items():
# 	print(f"Sinfdoshingiz {Familya.title()} {Ism} {Yosh}yoshda {Sinf}-Sinfda O'qiydi U Sinfdoshingiz {qoshimcha} U Sinfdoshingizning Qiziqishi {qoshimcha2}")		


# def salom_Ber():
# 	"""Salom Beruvchi Funksiya"""
# 	print("Assalomu Aleykum")

# salom_Ber()

# def salom_ber(ism):
# 	"""Foydalanuvchi Ismini Qabul Qilib, Unga Salom Beruvchi Funksiya"""
# 	print(f"Assalomu Aleykum, Hurmatli {ism.title()}!")

# salom_ber("Hasan")
# salom_ber("Murod")

# def toliq_ism(ism, familya):
# 	"""Foydalanuvchi Ism va Familyasini Jamlab Chiqaruvchi Funksiya"""
# 	print(
#          f"Foydalanuvchi ismi: {ism.title()}\n"
#          f"Foydalanuvchi familyasi: {familya.title()}"

# 	)

# toliq_ism('Olim', 'Hakimov')
# toliq_ism('Hakimov', 'Olim')

# def yosh_hisobla (tugilgan_yil, joriy_yil):
# 	"""Foydalanuvchini Tugilgan Yilini Hisoblovchi Dastur"""
# 	print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz" )

# yosh_hisobla(2004, 2021)

# def yosh_hisobla(ism, joriy_yil, tugilgan_yil):
# 	"""Foydalanuvchini Tugilgan Yilini Hisoblovchi Dastur"""
# 	# ism = input("Ismingizni Kiriting: ")
# 	# yosh  = input("Yoshingzni Kiriting: ")
# 	print(f"Siz {joriy_yil-tugilgan_yil} yilda tugilgansiz")

# yosh_hisobla('Utkir', 2021, 17)

def son_hisobla(son):
	"""Sonning Kvadratini Hisoblovchi Dastur"""
	print(f"{son} Sonning kvadrati {son**2} ga Teng")
	print(f"{son} Sonning Kubi {son**3} ga Teng")

son_hisobla(10)
