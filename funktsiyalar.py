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


# summa = 0
# i = 0
# while i < 6:
#     if i % 2 == 1:
#         summa += i
#         i += 2
#     else:
#         i += 1
# print(summa)

#1 data_user
# name = input('Ismingizni kiriting? >>> ')
# surname = input('Familiyangizni kiriting? >>> ')
# age = int(input('Yoshingizni kiriting? >>> '))
#
# def user_data():
#     print(f"""
#     *********************
#     *   Ismi: {name}        *
#     *   Familiyasi: {surname} *
#     *   Yoshi: {age}           *
#     ********************
# """)
# user_data()

#2
# a = int(input('A ni kiriiting? >>> '))
# b = int(input('B ni kiriiting? >>> '))
# c = int(input('C ni kiriiting? >>> '))

# def find_max(a, b, c):
#     if a == b == c:
#         print(f'Eng katta sonlar - A, B va C = {a}')
#     elif a == b > c:
#         print(f'Eng katta Sonlar - A va B = {a}')
#     elif a == c > b:
#         print(f'Eng katta Sonlar - A va C = {a}')
#     elif c == b > a:
#         print(f'Eng katta Sonlar - C va B = {c}')
#     elif a > b == c or a > b > c or a > c > b:
#         print(f'Eng katta son - A = {a}')
#     elif b > a == c or b > a > c or b > c > a:
#         print(f'Eng katta son - B = {b}')
#     elif c > a == b or c > a > b or c > b > a:
#         print(f'Eng katta son - C = {c}')
#     else: print('Error')
#
# find_max(a, b, c)

#3
# word = input('Sozlarni kiriting >>> ')
# letter = input('Qidirmoqchi bolgan sozni kiriting >>> ')

# def find_letter_count(w, l):
#     for l in w:
#         if l in w:
#             print(f'{w.count(l)} ta soz bor')
#             break
#         else: print('error')
#
# find_letter_count(word, letter)

#4
# def list_sum(mylist):
#     summa = sum(mylist)
#     return summa
# #     summa = 0
# #     for i in mylist:
# #         summa += i
# #     return summa
# #
# print("ro'yhat uchun sonlar kiriting: ")
# mylist = [int(i) for i in input().split()]
# print(list_sum(mylist))
# print(mylist)

#4
# mylist = int(input("Sonni kiriting"))


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


def max_sales(sales):
    if not sales:
        return "Malumot yoq"

    max_sale_month = None
    max_sale = None

    for key, value in sales.items():
        """dgiufbndfjgb"""
        if max_sale is None or value > max_sale:
            max_sale = value
            max_sale_month = key
            return