# 1. Svetafor: Foydalanuvchidan inputda svetavor qaysi rangda deb so’rang. qizil,
# sariq yoki yashil deb yozmoagunicha, bu xato rang deb qayta so’rayvering. Agar shu
# ranglardan birini tanlasa “rahmat, to’g’ri keladi” degan print chiqazing.

# while True:
#   svetafor = input("Svetavor qaysi rangda deb so'rang? ")
#   if svetafor == "qizil" or svetafor == "sariq" or svetafor == "yashil":
#       print("Rahmat, to'g'ri keladi")
#       break
#   else:
#     print("Xato rang!")

#2. Tasodifiy Sonni Topish O'yini: Kompyuter 1 dan 10 gacha bo'lgan tasodifiy son
# o'ylaydi. Foydalanuvchidan ushbu sonni topishni so'rang. Foydalanuvchi to'g'ri sonni
# topguncha davom etadi. Har bir noto'g'ri urinishdan so'ng, "Noto'g'ri, qayta urinib
# ko'ring" deb chiqaring. To'g'ri topilganda, "Tabriklaymiz, siz topdingiz!" deb chiqaring.
# Ko'rsatma: random. dan foydalanib tasodifiy son yarating va while sikli yordamida
# foydalanuvchi kiritmalarini tekshiring.

# import random
#
# raqamlar = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
#
# raqam = random.choice(raqamlar)
#
# taxminlar = set()
#
# while True:
#     chiqish = ''
#     for son in raqam:
#         if son in taxminlar:
#             chiqish += str(son)
#         else:
#             chiqish += '_'
#     print(chiqish)
#
#     if '_' not in chiqish:
#         print('Topdingiz!')
#         break
#     taxmin = input('Kompyuter oylagan sonni kiriting: ')
#     taxminlar.add(taxmin)
#     if taxmin not in raqam:
#         print('Xato')
#     else:
#         print('togri')
#
#     if len(taxminlar) >= 5:
#         print('Siz barcha imkoniyatdan foydalandingiz!')
#         break

#
# import random
#
# raqamlar = random.randint(1, 10)
# taxminlar = set()
# while True:
#     taxmin = int(input('Kompyuter oylagan sonni kiriting? >>> '))
#     if taxminlar == raqamlar:
#         print(f'Siz topdingiz! {raqamlar}')
#         break
#     else:
#         print('Xato topdingiz yana urinib koring')
#     taxminlar.add(taxmin)
#
#     if len(taxminlar) == 5:
#         print('Siz yutqazdingiz!')
#         break

#3
# ismlar = []
#
# while True:
#   ism = input("Do'stlaringizni ismini kiriting >>> ").lower()
#   if ism == 'stop':
#     print('Toxtadi')
#     break
#   else:
#     ismlar.append(ism)
#
# print(ismlar)

#4
# Usd = 12800
# Euro = 13500
# while True:
#     valyuta = input("Valyutani tanlang - Mavjd Valyutalar: Usd va Euro >>> ").title()
#     if valyuta == "Exit" or valyuta == "Stop":
#         break
#     elif valyuta == "Usd":
#         Usdd = int(input("Summa kiriting: "))
#         print(f"{Usdd / Usd} ni tashkil qiladi")
#     elif valyuta == "Euro":
#         Euroo = int(input("Summa kiriting: "))
#         print(f"{Euroo / Euro} ni tashkil qiladi")
#     else:
#         print("Error")


# While masala txt

#3
# While orqali Ro'yxatdagi 2-eng katta sonni topuvchi dastur yozing
def second_largest(raqamlar):
    if len(raqamlar) < 2:
        return None  # Agar ro'yxatda kamida 2 ta son bo'lmasa, None qaytaramiz

    eng_katta = float()  # Eng katta son uchun boshlang'ich qiymat
    ikkinchi = float()  # Ikkinchi eng katta son uchun boshlang'ich qiymat
    raqam = 0  # Ro'yxat bo'ylab yurish uchun indeks

    while raqam < len(raqamlar):
        son = raqamlar[raqam]
        if son > eng_katta:
            ikkinchi = eng_katta  # Eski eng kattani ikkinchi eng katta sifatida belgilaymiz
            eng_katta = son  # Yangi eng katta topildi
        elif eng_katta > son > ikkinchi:
            ikkinchi = son  # Ikkinchi eng katta topildi
        raqam += 1  # Keyingi elementga o'tish

    return ikkinchi # Natijani qaytarish

# print(second_largest([3, 5, 7, 2, 8]))  # Natija: 7
