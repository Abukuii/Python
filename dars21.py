# OOP darslari 1-dars
# 1 Oson1. "Oson1" nomli klass elon qiling. Bu klassda "a" integer o'zgaruvchi bor.
# output_a() - bu funksiya klassdagi "a" ni qiymatini print qilsin.

# num = int(input("Sonni kiriting >>> "))

class Oson1:
    def __init__(self, a):  # Konstruktor funksiyasi "a" qiymatini olish uchun
        self.a = a

    def output_a(self):  # Klassdagi "a" o'zgaruvchisini chop etadigan funksiya
        print(self.a)


# Klassdan obyekt yaratamiz
# obj = Oson1(num)  # "a" uchun qiymat sifatida 42 beriladi


# output_a funksiyasini chaqiramiz
# obj.output_a()  # Natija: 42


# 2 Oson2. "Oson2" nomli klass elon qililar. Bu klassda "a" va "b" integer o'zgaruvchilari bor.
# summa() - bu funksiya klassdagi "a" va "b" ni yig'indisini print qilsin.

class Oson2:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def summa(self):
        summ = (self.a + self.b)
        print(summ)


obj2 = Oson2(10, 15)


# obj2.summa()


# 3 Oson3. "Oson3" nomli klass elon qililar. Bu klassda "a" integer o'zgaruvchisi bor.
# plus_minus() - bu funksiya klassdagi "a" ni musbat yoki manfiy ekanligini print qilsin.

class Oson3:
    def __init__(self, a):
        self.a = a

    def plus_minus(self):
        son = self.a
        if son > 0:
            print(f"{son} musbat")
        else:
            print(f"{son} manfiy")


# obj3 = Oson3(num)


# obj3.plus_minus()


# 4 Oson4. "Oson4" nomli klass elon qililar. Bu klassda "a" integer o'zgaruvchi bor.
# odd_even() - bu funksiya klassdagi "a" ni to'g yoki juft ekanligini print qilib bersin.

class Oson4:
    def __init__(self, a):
        self.a = a

    def odd_even(self):
        son = self.a
        if son == 0:
            print("Bu nol")
        elif son < 0:
            print(f"{son} Bu son manfiy")
        elif son % 2 != 0:
            print(f'{son} Odd')
        else:
            print(f"{son} Even")


# obj4 = Oson4(num)


# obj4.odd_even()


# 5 Oson5. "Oson5" nomli klass elon qililar. Bu klassda "a" va "b" integer o'zgaruvchisi bor.
# daraja() - bu funksiya klassdagi "a" ni "b" chi darajasini print qilsin.

class Oson5:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def daraja(self):
        pow = self.a ** self.b
        print(pow)


# obj5 = Oson5(num, 2)


# obj5.daraja()


# 6 6. "MyClass6" nomli klass elon qililar. Bu klassda "words" list bo'sh o'zgaruvchisi bor.
# add_word(word) - bu funksiya "words" ga element qo'shib qo'ysin.
# remove(word) = bu funksiya "words" da "word" ni o'chirib tashlasin.

class Myclass6:
    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)
        print(f"{word} append")

    def remove_word(self, word):
        if word in self.words:
            self.words.remove(word)
            print(f"{word} remove")
        else:
            print(f"{word} not found ")


obj6 = Myclass6()


#
# obj6.add_word("Welcome")
# obj6.add_word("Word")

# print(obj6.words)

# obj6.remove_word("Word")

# print(obj6.words)

# 7 7. "MyClass7" nomli klass elon qiling. Bu klassda bo'sh "myDict" dictionary o'zgaruvchisi bor.
# add_elem(key, val) - bu funksiya "myDict" "key" ni qiymatiga teng bo'lgan key bo'lmasa "val" ni add qilsin,
# bor bolsa xech narsa qilmasin.
# update_elem(key, val) - bu funksiya "myDict" shu "key" ni qiymatiga teng bolgan key bo'lsa "val" ni update qilsin,
# yoq bolsa xech narsa qilmasin.

class Myclass7:
    def __init__(self):
        self.myDict = {"Abukuii": 18, }

    def add_elem(self, key, val):
        if key not in self.myDict:
            self.myDict[key] = val
            print(f"{key} add dict")

    def update_elem(self, key, val):
        if key in self.myDict:
            self.myDict[key] = val
            print(f"{key} update")


obj7 = Myclass7()


# obj7.add_elem("Abuku", 22)
# obj7.add_elem("Otabek", 21)
# print(obj7.myDict)
#
# obj7.update_elem("Abuku", 20)
# print(obj7.myDict)

# 8. "MyClass8" nomli klass elon qililar. Bu klassdan "numbers" list o'zgaruvchisi bor.
# compare_lists(new_list) - bu funksiya klassdagi "numbers" ni elementlar yig'indisi
# "new_list" ni elementlar yig'indisidan katta aniqlab katta listni print qilsin.

# class MyClass8:
#     def __init__(self):
#         self.numbers = [1, 2, 3, 4, 5]
#
#     def compare_list(self, new_list):
#         if sum(self.numbers) > sum(new_list):
#             print('Numbers katta')
#         elif sum(self.numbers) < sum(new_list)
#             print("New List katta")
#         else:
#             print("Ikkalasi teng")


# obj8 = MyClass8()


# obj8.compare_list([1, 2, 3, 4, 4])

# 9. "MyClass9" nomli klass elon qililar. Bu klassdan "list1" va "list2" list o'zgaruvchilari bor.
# list1_max() - bu funksiya klassdagi "list1" dan maximumni topib return qilsin.
# list2_max() - bu funksiya klassdagi "list2" dan maximumni topib return qilsin.
# sum_of_two_max() - bu funksiya klassdagi list1_max() va list2_max() foydalanib ikkita maximumni topib yig'indisini print qilsin.


# class MyClass9:
#     list1 = [1, 2, 3, 4, 46, 6, ]
#     list2 = [1, 2, 3, 4, 48, 6, ]
#
#     def list1_max(cls):
#         return max(cls.list1)
#
#
#     def list2_max(cls):
#         return max(cls.list2)
#
#
#     def sum_of_max_two(cls):
#         max1 = max(cls.list1)
#         max2 = max(cls.list2)
#         return max2 + max1


# obj9 = MyClass9()

#
# print(obj9.list1_max())
# print(obj9.list2_max())
# print(obj9.sum_of_max_two())


class MyClass9:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def list1_max(self):
        return max(self.list1)

    def list2_max(self):
        return max(self.list2)

    def sum_of_two_max(self):
        max1 = self.list1_max()
        max2 = self.list2_max()
        print(f"Sum of max values: {max1 + max2}")


# # Klassdan foydalanish
# obj = MyClass9([1, 5, 3, 7], [10, 2, 8, 6])
# obj.sum_of_two_max()  # Bu list1 va list2 maksimumlari yig'indisini chop etadi


# 10. "MyClass10" nomli klass elon qililar. Bu klass "numbers" list o'zgaruvchilari bor.
# divide(d) - bu funksiya klassadagi "numbers" list elementlarini "d" qoldiqsiz bo'linsa bitta list yig'sin funksiyani ichida.
# va funksiya oxirida bolinadigonlarni listini return qilsin.


class MyClass10:
    def __init__(self):
        self.numbers = []

    def divide(self, d):
        bolinma = [i for i in self.numbers if i % d == 0]
        return bolinma


obj10 = MyClass10()

obj10.numbers = [2, 3, 4, 5, 6, 6, 7, 8]
print(obj10.divide(2))
