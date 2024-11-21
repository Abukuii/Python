# 10 dars for sikli

#1
# pochtalar = ['user1@gmail.com', 'user2yahoo.com', 'user3outlook.com']
#
# if len(pochtalar) > 0:
#     for pochta in pochtalar:
#         if pochta.find('@') != -1 and pochta.find(".") != -1:
#             print(f"{int(pochtalar.index(pochta)) + 1} - email manzili {pochta} Qabul qilindi")
#         else: print(f"{int(pochtalar.index(pochta)) + 1} - email manzili {pochta} Bu pochta qabul qilinmadi")

#2
# password = ["password123", "Qwerty!", "admin", "StrongPass1!"]

# if len(password) > 0:
#     for pas in password:
#         if len(pas) < 8:
#             print(f"{pas} Juda qisqa")
#         elif len(pas) >= 8 and pas.isascii() == False:
#             print(f"{pas} Kuchsiz parol")
#         else: print(f"{pas} Kuchli parol")

#3
# ob_havo = [20, 22, 19, 24, 25, 23, 21]
#
# if len(ob_havo) > 0:
#     for kun in ob_havo:
#         if int(kun) > 22:
#             print(f"{ob_havo.index(kun) + 1} kun  Iliq kun")
#         else: print(f"{ob_havo.index(kun) + 1} kun Salqin kun")
#
# hafta = len(ob_havo)
# natija = 0
# for kun in ob_havo:
#     natija += kun
# natija /= hafta
# if natija > 22:
#     print(f"Haftalik natija {natija} bu hafta iliq boldi")
# else:
#     print(f"Haftalik natija {natija} bu hafta salqin boldi")

#4
# taomlar =  ["Osh", "Shashlik", "Manti", "Lagmon",]
# buyurtma = input("Nima buyurtma berasiz? >>> ").title()
#
# if len(taomlar) > 0:
#         if buyurtma in taomlar:
#             print("Buyurtmangiz qabul qilindi")
#         else: print("Kechirasiz bizda bunday taom yoq")

#5
# users = [16, 21, 17, 30, 25]
#
# if len(users) > 0:
#     for user in users:
#         if user < 18:
#             print(f"Hurmatli {users.index(user) + 1} - foydalanuvchi, siz Yosh chegarasiga yetmagansiz ")
#         else: print(f"Hurmatli {users.index(user) + 1} - foydalanuvchi, Xush kelibsiz")

#6
# xabarlar=["Yangi xabar", "Batareya past", "Yangilanish mavjud"]
# xabar = "Batareya past"
#
# if len(xabarlar) > 0:
#     if xabar in xabarlar:
#         print("Telefonni zaryadlang")
#     else: print("Error")

#7
fayllar = ["kitob.jpg", "ko'k_jiguli.mp3", "tabiat.jpg", "malohat.mp3", "iphone16.jpg"]
musiqalar = []
rasmlar = []

# if len(fayllar) > 0:
#     for fayl in fayllar:
#         if fayl.find(".mp3") != -1:
#             musiqalar.append(fayl)
#             print(f"{fayllar.index(fayl) + 1} - fayl musiqalarga qo'shildi!")
#         else:
#             rasmlar.append(fayl)
#             print(f"{fayllar.index(fayl) + 1} - fayl rasmlarga qo'shildi")
#
# print(musiqalar)
# print(rasmlar)

"""
foydalanuvchidan qiziqishlari so'ralsin.

Agar kitob yoki kutubxona qiziqishlari orasida bo'lsa, qanday kitoblar yoqishi so'ralsin.
    agar detektiv so'zini ishlatsa, shaytanat kitobi haqidagi fikri so'ralsin.
    agar diniy kitoblarga qiziqsa "Hadis va Hayot" kitoblar to'plamini sovg'a qilamiz deyilsin.

Agar sport so'zi qiziqishlari orasida bo'lsa, qaysi sport turiga qiziqishi so'ralsin,
   agar futbol sport turlari orasida bo'lsa, qaysi komandani yoqtirishi so'ralsin.
        agar real yoki barsa komandasini yozsa, el-classicoga chipta sovg'a qilamiz deyilsin
"""

# ism = input("Ismingiz >>> ")
# qiziqishlari = input(f"Salom {ism}, Nimalarga qiziqasiz >>> ")
#
# for qiziqish in qiziqishlari:
#     if qiziqish.find('kitob') != -1 or qiziqish.find('kutubxona') != -1:
#         savol = input(f'{ism} sizga qanday kitoblar yoqadi? >>> ')
#         for tur in savol:
#             if tur.find('detektiv') != -1:
#                 savol1 = input(f'{ism} Shaytanat kitobi haqida fikringiz >> ')
#                 print('Ajoyib fikrlar uchun rahmat')
#             elif tur.find('diniy') != -1:
#                 print('Sizga Hadis va hayot kitobini sovga qilamiz')
#                 break
#     elif qiziqish.find('sport') != -1:
#         savol2 = input(f'{ism} Qaysi sport turiga qiziqasiz? >>> ')
#         for sport in savol2:
#             if sport.find('futbol') != -1:
#                 savol3 = input(f'{ism} qaysi jamoaga muxlislik qilasiz >>> ')
#                 for jamoa in savol3:
#                     if jamoa.find('real') != -1 or jamoa.find('barsa') != -1:
#                         print('El classico ga sovga qilamiz!')
#     else: print('Error')