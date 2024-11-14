# List Compehension Lambda Map Reduce Filter funksiyalari haqida

# List Compehension
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
toqlar = [i for i in l if i % 2 == 0]
# print(toqlar)

#1 M. Samolyot uchuvchi va qo'nuvchi viloyatlar korsatilgan. Topshiriq: Uchib ketuvchi viloyatlarni chiqaring
regions = [["Toshkent", "Buxoro"], ["Farg'ona", "Jizzax"], ["Jizzax", "Navoiy"], ["Andijon", "Farg'ona"],
           ["Samarqand", "Andijon"], ["Buxoro", "Samarqand"]]
FromCity = [l[1] for l in regions]
# print(FromCity)

#2
# 2-misol Ushbu toq sonlarni 2ga ko'paytirib yangi listga o'tkazing
sonlar = [1, 2, 3, 4, 5]
pow = [i**2 for i in sonlar]
# print(pow)

#3 - misol
# Listdagi malum elementning ilk uchragan indexini topish
listt = ['Alice', 1, 'Alice', 2, 3, 'Alice']

indice = listt.index('Alice')
# print(indice)

#listdagi malum elementning barcha indexini topish
indice = [i for i in range(len(listt)) if listt[i] == 'Alice']
# print(indice)

#4 - misol
# (ism $ pul) Millionerni toping.
people = [('John', 240_000), ('Alice', 1_000_000), ('Doe', 1_000_000), ('Ann', 240_000)]
millioners = [name for name, money in people if money >= 1_000_000]
# print(millioners)

def find_millioners(people):
    return [name for name, money in people.items() if money >= 1_000_000]

people_data1 = {'John': 250_000, 'Alice': 1_000_000, 'Bob': 998_170, 'Carol': 1_229_080, 'Frank': 881_230, 'Eve': 93_121}
people_data2 = {'John': 250_000, 'Alice': 1_000_000, 'Bob': 998_170, 'Frank': 1_881_230, 'Eve': 93_121}

def test():
    assert find_millioners(people_data1) == ['Alice', 'Carol']
    assert find_millioners(people_data2) == ['Alice', 'Eve']
# test()

#5 - miisol
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

l = []
for x in range(3):
    for y in range(3):
        l.append((x, y))
# print(l)

#6 - misol
# Matns=dan uzunligi 5ta harfdan ortiq bo'lgan so'zlarni toping
text = '''Call me Ishmael. Some ears ago - never mind hov long precisely - having lettle
or no money in my purse, and nothing particular to intersted me on shore, I tohught I 
would sail about a little and see the watery part of the world. It is a way I have of driving off
the spleen, and regulating the circulation. - Moby Dick'''
# print([i for i in text.split() if len(i) >= 7])
# print([[i for i in line.split() if len(i) >= 7] for line in text.split("\n")])

# Ziplash
list1 = ['ism', 'familiya', 'yosh']
list2 = ['Akmal', 'Tohirov', 16]

dictt = [{k, v} for k, v in zip(list1, list2)]
# print(dictt)

#7 - misol
# Ustun  nomlari va qtorlarni birlashitirish

cols = ['Name', 'Salary', 'Jobs']
rows = [('Alice', 180_000, 'Data Scientist'),
        ('Bob', 90_000, 'Project Manager'),
        ('Frank', 87_000, 'Backend Developer')]
# db = [dict(zip(cols, row)) for row in rows]
# db = [dict(zip(cols, rows))]
# print(db)

# lambda
# f = lambda a: a*2
# # ==
# def f(a):
#     return a**2

#8 - misool
#3ta son yigindisini toping
#
# summ = lambda a, b ,c: a+b+c
# print(summ(1,2,3))

# print((lambda a, b, c: a + b + c)(1,2,3))
# print((lambda a,b,: a+b+10)(1,2))

def summa(a, b, c):
    return a + b + c
# print(summa(2,5,7))

#Map()
#yigindilarni qo'shib chiqadi
#malumotlarni o'zgartiradi

#9 - misol
# str_nums = ['1', '2', '3', '4', '5', '6', '7']
# int_nums = list(map(int, str_nums))
# print(int_nums)

str_num1 = ['1', '2', '3', '4', '5', '6', '7']
nums = list(map(int, str_num1))
# print(nums)

#10 - misol
# Sonlarni kvadratga ko'taring

nums1 = [1, 2, 3, 4, 5, 6]
# print(list(map(lambda x: x**2, nums1)))

#11 - misol
# Listdagi elementlarni mos indexi bo'yicha ayiring
# print(list(map(lambda x, y: x - y, [2, 3, 5], [1, 2, 4])))

#12 - MISOL
# lISTDAGI elementlarni katta harfga o'tkazing
text1 = ['processing', 'strings', 'with', 'map']
# print(list(map(str.upper, text1)))

#13 - misol Faktorial\
# Reduce()
from functools import reduce

n = 5
# print(reduce(lambda x, y: x * y, range(1, n + 1)))