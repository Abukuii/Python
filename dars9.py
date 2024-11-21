#1
# obhavo = int(input("Hozir Ob havo necha graduc C? >>> "))
#
# if obhavo < 0:
#     print("Sovuq")
# elif obhavo >= 0 and obhavo <= 20:
#     print("Salqin")
# elif obhavo > 20 and obhavo < 30:
#     print("Iliq")
# else:
#     print("Issiq")

#2
# chegirma = int(input("Jami Xarid Summangiz? >>> "))
# besh = chegirma * 5/100
# on = chegirma * 10/100
#
# if chegirma > 0 and chegirma < 50000:
#     print("Xurmatli mijoz uzur Sizga Chegirma yoq")
# elif chegirma >= 50000 and chegirma <= 100000:
#     print("Xurmatli mijoz Sizga 5% chegirma bor")
#     print(f"Xurmatli mijoz jami to'lovingiz {chegirma - besh} so'm")
# elif chegirma > 100000:
#     print("Xurmatli mijoz sizga 10% chegirma bor")
#     print(f"Xurmatli mijoz Jami to'lovingiz {chegirma - on} so'm")
# else:
#      print("Error")
# print("Xaridingiz uchun tashakkur!!!")

#3
# login = input("Loginni kiriting? >>> ")
# parol = int(input("Parolni kiriting? >>> "))
# login1 = "admin"
# parol1 = 12345

# if login == login1 and parol == parol1:
#     print("Welcome")
# else:
#     print("Login Yoki parol xato!!!")


#
# if login == login1 and parol == parol1:
#     print("Welcome")
# elif login == login1 and parol != parol1:
#     print("Kiritilgan Parol Noto'gri Qaytadan urinib ko'ring!")
# elif login != login1 and parol == parol1:
#     print("Kiritilgan Login Noto'gri Qaytadan urinib ko'ring!")
# else:
#     print("Bunday foydalanuvchi mavjud emas!!!")

#4
# age = int(input("Necha Yoshsiz? >>> "))
#
# if age < 13:
#     print("Sizga bu kinoni ko'rish tavsiya etilmaydi")
# elif age >= 13 and age <= 17:
#     print("Siz filmni ota-onangiz bilan ko'rishingiz mumkin")
# else:
#     print("Siz filmni tomosha qilishingiz mumkin")

#5
# menu = int(input("Assalomu Alekum Xurmatli mijoz. Restoranimizga xush kelibsiz! Menu: 1). Osh, 2). Mastava, 3). Shashlik. Nima buyurtma berasiz >>>"))
# vazifa = "Yoqimli Ishtaha!..."
# if menu == 1:
#     print("Xurmatli Mijoz Osh narxi 18 000 so'm va u 10 daqiqada tayyor boladi ")
#     print(vazifa)
# elif menu == 2:
#     print("Xurmatli Mijoz Mastava narxi 15 000 so'm va u 5 daqiqada tayyor bo'ladi")
#     print(vazifa)
# elif menu == 3:
#     print("Xurmatli Mijoz Shashlik narxi 12 000 so'm va u 7 daqiqada tayyor bo'ladi")
#     print(vazifa)
# else:
#     print("Error! Iltimos menudagi raqamlardan foydalaning!!!")

#6
# email = input("Emailingizni kiriting! >>> ")
# if email.find("@")==-1 or email.find(".")==-1:
#     print("Noto'g'ri email manzili!")
# else:
#     print("Email qabul qilindi!")

# email = input("Emailingizni kiriting! >>> ")
# lis = []
# lis.extend(email)
# print(lis)
# if '@' in lis and '.' in lis:
#     print("Email qabul qilindi")
# else:
#     print("Noto'gri email!")

#7
# ball = int(input("To'plagan balingizni kiriting >>> "))
#
# if ball >= 86 and ball <= 100:
#     print("5 baho")
# elif ball >= 70 and ball <= 85:
#     print("4 baho")
# elif ball >= 55 and ball <= 69:
#     print("3 baho")
# elif ball < 55:
#     print("2 baho")
# else: print("Error! Bunday Bal Mavjud emas...")

#8
# karta = int(input("Kartadagi Summa? >>> "))
# naqd = int(input("Qancha Pul yechmoqchisz? >>> "))
#
# if karta < naqd:
#     print(f"Hisobingizda mablag' yetarli emas? Hisobingizda {karta} so'm mavjud")
# elif karta < 5000:
#     print(f"Minimal Pul yechish summasi 5000. Hisobingizda {karta} so'm mavjud")
# else:
#     print(f"Pul Muvaffaqiyatli yechildi! Hisobingizda {karta - naqd} so'm qoldi")

#9
# haftanomi = input("Bugun haftaning qaysi kuni? >>> ").capitalize()
# bir = "Dushanba"
# ikki = "Seshanba"
# uch = "Chorshanba"
# tort = "Payshanba"
# besh = "Juma"
# olti = "Shanba"
# yetti = "Yakshanba"
# ish = "Ish kuni"
# dam = "Dam olish kuni"
#
# if haftanomi == olti or haftanomi == yetti or haftanomi == "bozor":
#     print(f"Bugun {haftanomi}, {dam}")
# elif haftanomi == bir or haftanomi == ikki or haftanomi == uch or haftanomi == tort or haftanomi == besh:
#     print(f"Bugun {haftanomi}, {ish}")
# else:
#     print("Error! Kechirasiz Bunday Hafta kuni mavjud emas!... ")

# haftkuni = int(input("Bugun haftaning nechinchi kuni? >>> "))
#
# if haftkuni == 1:
#     print(f"Bugun {bir}, {ish}")
# elif haftkuni == 2:
#     print(f"Bugun {ikki}, {ish}")
# elif haftkuni == 3:
#     print(f"Bugun {uch}, {ish}")
# elif haftkuni == 4:
#     print(f"Bugun {tort}, {ish}")
# elif haftkuni == 5:
#     print(f"Bugun {besh}, {ish}")
# elif haftkuni == 6:
#     print(f"Bugun {olti}, {dam}")
# elif haftkuni == 7:
#     print(f"Bugun {yetti}, {dam}")
# else:
#     print("Error! Bunday ish kuni mavjud emas!...")

# tarif = int(input("Oyiga Qancha internet sarflaysiz? (GB) >>> "))
#
# if tarif <= 1:
#     print("Sizga Mini tarifi mos keladi")
# elif tarif > 1 and tarif <= 5:
#     print("Sizga Standart tarifi mos keladi")
# else: print("Sizga Unlimited tarifi mos keladi")

# Otabek Nematov
