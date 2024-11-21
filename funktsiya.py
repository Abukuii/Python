# print('hello world')
#
# def ikki_va_uch ():
#     for i in range(1, 40):
#         if i % 2 == 0 and i % 3 == 0:
#             print(f'{i} 2 va 3 ga bo\'linadi')
#
# ikki_va_uch()


# def mylist():
#     while True:
#         son = int(input("Sonni kirit >>>"))
#         summa = 0
#         if son == 0:
#             print(summa)
#             break
#         else:
#             summa += son
#             print('son qoshildi! ')
#
# mylist()
#
# def digit_count_and_sum(word):
#     # Raqamlarning yig'indisini hisoblash
#     # Raqamlarning yig'indisini hisoblash uchun boshlang'ich qiymat
#     d_sum = 0
#     d_count = 0
#
#     # Har bir belgini tekshirish uchun sikl
#     for char in word:
#         # Agar belgi raqam bo'lsa
#         if char.isdigit():
#             # Belgini raqam (integer) ko'rinishiga o'tkazamiz va d_sum ga qo'shamiz
#             d_sum += int(char)
#             d_count += 1
#
#
#     return f"Sonni yig'indisi {d_sum}, soni {d_count} ta"
#
#
# nom = 'w3o4r5d'
# print(digit_count_and_sum(nom))

# Funktsiyalar
# darsda so'ralgan masalaga yechim
# def uzbek_number(num):
# #
# #     ones = ['bir', 'ikki', 'uch', 'to\'rt', 'besh', 'olti', 'yetti', 'sakkiz', 'to\'qqiz']
# #     tens = ['', 'o\'n', 'yigirma', 'o\'ttiz', 'qirq', 'ellik', 'oltmish', 'yetmish', 'sakson', 'to\'qson']
# #     if num == 0: return "nol"
# #     if num < 10:
# #         return ones[num-1]
# #     elif num < 20:
# #         return 'o\'n ' + ones[num % 10-1]
# #     elif num < 100:
# #         return tens[num // 10] + (' ' + ones[num % 10-1] if num % 10 != 0 else '')
# #     elif num < 1000:
# #         return ones[num // 100-1] + ' yuz ' + uzbek_number(num % 100)
# #     elif num < 1_000_000:
# #         return uzbek_number(num // 1_000) + ' ming ' + uzbek_number(num % 1_000)
# #     elif num < 1_000_000_000:
# #         return uzbek_number(num // 1_000_000) + ' million ' + uzbek_number(num % 1_000_000)
# #     elif num < 1_000_000_000_000:
# #         return uzbek_number(num // 1_000_000_000) + ' milliard ' + uzbek_number(num % 1_000_000_000)
# #
# #     else:
# #         return 'Xato raqam'
# #
# # print(uzbek_number(2112401001))
# from curses.ascii import isalnum, isdigit

# from hangman_game import letter


# summa = 0
# i = 0
# while i < 6:
#     if i % 2 == 1:
#         summa += i
#         i += 2
#     else:
#         i += 1
# print(summa)

def ikiuch():
    for i in range(1, 41):
        if i % 2 == 0 and i % 3 == 0:
            print(i)
# ikiuch()

royxat = {
    "yanvar": 12000,
    'fevral': 6000,
    'aprel': 15000,
    'sentabr': 9000,
    'dekabr': 10000,
}

def big_sales(sales):
    max_month = None
    max_money = 0
    for month, money in sales.items():
        if money > max_money:
            max_money = money
            max_month = month
    return max_month
# print(big_sales(royxat))

def max_sale(sales):
    return max(sales, key=sales.get)
print(max_sale(royxat))