# 10 dars for sikli

#1
# pochtalar = ['user1@gmail.com', 'user2yahoo.com', 'user3outlook.com']
#
# if len(pochtalar) > 0:
#     for pochta in pochtalar:
#         if pochta.find('@') != -1:
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