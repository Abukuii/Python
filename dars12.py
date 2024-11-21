
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
#
#
# #     summa = 0
# #     for i in mylist:
# #         summa += i
# #     return summa
# #
# print("ro'yhat uchun sonlar kiriting: ")
# mylist = [int(i) for i in input().split()]
# print(list_sum(mylist))
# print(mylist)


#5
# son = int(input("Sonni kiriting >>> "))
# daraja = int(input("darajasini kiriting >>> "))
#
# def sonni_darajasi(s, d):
#     """Sonni darajasini chiqarib beruvchi funktsiya"""
#     pow = s ** d
#     return pow
#
# print(sonni_darajasi(son, daraja))


#6
# son1 = int(input('A Sonni kiriting >>> '))
# daraja1 = int(input("A Darajani kiriting >>>"))
# son2 = int(input('B Sonni kiriting>>> '))
# daraja2 = int(input("B Darajani kiriting >>>"))
#
# def sonni_darajalari(s1, s2, d1, d2):
#     pow = s1 ** d1, s2 ** d2
#     return pow
# print(sonni_darajalari(son1, son2, daraja1, daraja2))


#7

def digit_count_and_sum(word):
    # Raqamlarning yig'indisini hisoblash
    # Raqamlarning yig'indisini hisoblash uchun boshlang'ich qiymat
    d_sum = 0
    d_count = 0

    # Har bir belgini tekshirish uchun sikl
    for char in word:
        # Agar belgi raqam bo'lsa
        if char.isdigit():
            # Belgini raqam (integer) ko'rinishiga o'tkazamiz va d_sum ga qo'shamiz
            d_sum += int(char)
            d_count += 1

    return f"Sonni yig'indisi {d_sum}, soni {d_count} ta"


# nom = 'w3o4r5d'
# print(digit_count_and_sum(nom))

#8
def add_right(a, b):
    return str(a) + str(b)

# print(add_right(5, 6))

#9
def add_left(a, b):
    return str(b) + str(a)

# print(add_left(5, 6))


#10
def work_with_list(a):
    m = min(a)
    for i in range(len(a)):
        a[i] *= m
    return a

# print(work_with_list([3,5,7]))

#11
example = {
    "yanvar": 12000,
    "fervral": 6000,
    "aprel": 15000,
    "sentabr": 9000,
    "dekabr": 10000,
}

def max_sales(sales):
    if not sales:
        return "Malumot yoq"

    max_sale_month = None
    max_sale = None

    for key, value in sales.items():
        """Eng kop sotilgan oyni aniqlovchi funksiya"""
        if max_sale is None or value > max_sale:
            max_sale = value
            max_sale_month = key

    return max_sale_month

# print(max_sales(example))

#12

def min_max(numbers, max_num, min_num):
    max1 = max(numbers)
    min1 = min(numbers)
    if max1 == max_num:
        print("to'gri topdingiz")
    else: print("Xato")
    if min1 == min_num:
        print("togri topdingiz")
    else: print("xato")

# min_max([1,2,3,5,7], 7, 1)


#13
def expensiveProducts(products):
    price = 0
    name1 = None

    for product in products:
        if product["price"] > price:
            price = product["price"]
            name1 = product["name"]

    return name1

arr = [
    {
        "name": "Iphone X",
        "price" : 600
    },
{
        "name": "Iphone 12",
        "price" : 1500
    },
{
        "name": "Iphone Samsung note 9",
        "price" : 800
    },
]

print(expensiveProducts(arr))
