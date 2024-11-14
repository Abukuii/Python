# Dictionary metodlari copy va deepcopy

from collections import Counter



#1
# 1. stringlar ro'yxatini oladigan va ularni uzunligi bo'yicha guruhlaydigan str_counter(strs) funksiya yozing,
# bunda kalitlar string uzunliklari va qiymatlar shu uzunlikdagi string keladi.
# M: str_counter(["shaftoli", "olma", "nok" ]) -> {8:"shaftoli", 4: "olma", 3: "nok"}

def str_counter(strs):
    """So'zlarni uzunligini aniqlaydigan funksiya"""
    result = {}
    for str in strs:
        length = len(str)  # 1. String uzunligini aniqlaymiz
        if length in result:
            # 2. Agar uzunlik allaqachon lug'atda mavjud bo'lsa, shu uzunlikka mos stringni qo'shamiz
            result[length].append(str)
        else:
            # 3. Agar uzunlik lug'atda bo'lmasa, yangi ro'yxat yaratib, birinchi stringni qo'shamiz
            result[length] = [str]
    return result

# print(str_counter(["shaftoli", "olma", "nok", "anor", "banan"]))

def group_by_parity(numbers):
    """Sonlarni juft yo toq ekanligini aniqlaydigan funksiya"""
    result = {"even": [], "odd": []}  # Juft va toq sonlar uchun bo'sh ro'yxatlarni yaratamiz
    for number in numbers:
        if number % 2 == 0:
            result["even"].append(number)  # Juft sonlarni "even" kalitiga qo'shamiz
        else:
            result["odd"].append(number)   # Toq sonlarni "odd" kalitiga qo'shamiz
    return result

# print(group_by_parity([1, 2, 3, 4, 5, 6, 7, 8]))



#2
# 2. Bir xil uzunlikdagi ikkita listni parametr sifatida oladigan, kalitlar birinchi ro'yxatning
# elementlari va qiymatlar ikkinchi ro'yxatning mos keladigan elementlari bo'lgan dict qaytaradigan merge_list(l1,l2) funksiya yarating.

def merge_list(l1, l2):
    if len(l1) != len(l2):
        raise ValueError("Ro'yxatlar uzunligi bir xil bo'lishi kerak")  # Agar uzunliklar mos kelmasa, xatolik chiqaramiz
    result = {}  # Natija uchun bo'sh lug'at yaratamiz
    i = 0  # Ro'yxat bo'ylab yurish uchun indeks
    while i < len(l1):
        result[l1[i]] = l2[i]  # l1'ning i-elementini kalit, l2'ning i-elementini qiymat qilib qo'shamiz
        i += 1  # Keyingi elementga o'tamiz
    return result


# def merge_list(l1, l2):
#     if len(l1) != len(l2):
#         raise ValueError("Ro'yxatlar uzunligi bir xil bo'lishi kerak")  # Uzunliklar mos kelmasa, xatolik chiqaramiz
#     return dict(zip(l1, l2))  # zip yordamida juftliklar yaratamiz va dict orqali lug'atga o'giramiz

list_1 = ["a", "b", "c"]
list_2 = [1, 2, 3]
# print(merge_list(list_1, list_2))  # Natija: {"a": 1, "b": 2, "c": 3}


#3
# 3. Foydalanuvchilarga kontaktlarni qo‘shish, yangilash, o‘chirish va qidirish
# imkonini beruvchi dict ga asoslangan telefon kontaktlar ro'yxati dasturini yarating
# M: contacts = {"Nodir":"+998918602711", "Laziz":"+998908002534"}

def add_contact(contacts, name, number):
    """Yangi kontakt qo'shish funksiyasi."""
    contacts[name] = number
    print(f"{name} kontakti qo'shildi.")


def update_contact(contacts, name, new_number):
    """Kontaktni yangilash funksiyasi."""
    if name in contacts:
        contacts[name] = new_number
        print(f"{name} kontakti yangilandi.")
    else:
        print(f"{name} kontakt topilmadi.")


def delete_contact(contacts, name):
    """Kontaktni o'chirish funksiyasi."""
    if name in contacts:
        del contacts[name]
        print(f"{name} kontakti o'chirildi.")
    else:
        print(f"{name} kontakt topilmadi.")


def search_contact(contacts, name):
    """Kontaktni qidirish funksiyasi."""
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"{name} kontakt topilmadi.")


def display_contacts(contacts):
    """Barcha kontaktlarni ko'rsatish funksiyasi."""
    if contacts:
        print("Kontaktlar ro'yxati:")
        for name, number in contacts.items():
            print(f"{name}: {number}")
    else:
        print("Kontaktlar ro'yxati bo'sh.")


def main():
    contacts = {"Nodir": "+998918602711", "Laziz": "+998908002534"}
    while True:
        print("\n1. Yangi kontakt qo'shish")
        print("2. Kontaktni yangilash")
        print("3. Kontaktni o'chirish")
        print("4. Kontaktni qidirish")
        print("5. Barcha kontaktlarni ko'rish")
        print("6. Dasturni to'xtatish")

        choice = input("Tanlang (1-6): ")

        if choice == "1":
            name = input("Kontakt nomi: ")
            number = input("Telefon raqami: ")
            add_contact(contacts, name, number)

        elif choice == "2":
            name = input("Yangilanadigan kontakt nomi: ")
            new_number = input("Yangi telefon raqami: ")
            update_contact(contacts, name, new_number)

        elif choice == "3":
            name = input("O'chiriladigan kontakt nomi: ")
            delete_contact(contacts, name)

        elif choice == "4":
            name = input("Qidiriladigan kontakt nomi: ")
            search_contact(contacts, name)

        elif choice == "5":
            display_contacts(contacts)

        elif choice == "6":
            print("Dastur to'xtatildi.")
            break
        else:
            print("Noto'g'ri tanlov, qaytadan urinib ko'ring.")


# Dasturni ishga tushirish
main()

#4
# 4. Raqamlar ro'yxatini oladigan va ro'yxatdagi har bir raqamning takrorlanish sonini o'z ichiga
# olgan dict qaytaradigan counter_dict(nums) nomli funksiya yozing.
# M: counter_dict([2,1,1,1) -> {2:1, 1:3} Chunki listda 1ta 2 va 3ta 1bor.

def counter_dict(nums):
    """Raqamlar ro'yxatidagi har bir raqamning takrorlanish sonini hisoblaydigan funksiya."""
    return dict(Counter(nums))

# 2)
# def counter_dict(nums):
#     """Raqamlar ro'yxatidagi har bir raqamning takrorlanish sonini hisoblaydigan funksiya."""
#     counts = {}  # Bo'sh lug'at yaratamiz
#     for num in nums:
#         if num in counts:  # Agar raqam allaqachon lug'atda bo'lsa
#             counts[num] += 1  # Takrorlanish sonini oshiramiz
#         else:
#             counts[num] = 1  # Agar raqam birinchi marta uchrasa, 1 qiymatni beramiz
#     return counts

# Misol
nums = [2, 1, 1, 1]
result = counter_dict(nums)
# print(result)  # {2: 1, 1: 3}


#5
# 5. Ballar dict ni(kalit = talaba nomi, qiymat = ball) parametr sifatida oladigan va eng yaxshi ikkita
# o'quvchining ismlari ro'yxatini qaytaradigan max_ball_students(talabalar) funksiya yozing.
# max_ball_students({"Akmal":64, "Tohir":55, "Nodir":76, "Zafar":80 }) -> {"Zafar":80, "Nodir":76}

def max_ball_students(talabalar):
    """Eng yaxshi ikkita o'quvchining ismlari va ballarini qaytaruvchi funksiya."""
    # Talabalarni ballar bo'yicha saralash (eng katta ballar birinchi bo'ladi)
    sorted_students = sorted(talabalar.items(), key=lambda item: item[1], reverse=True)

    # Eng yaxshi ikkita o'quvchini olish
    top_two = sorted_students[:2]

    # Natijani lug'at sifatida qaytarish
    return dict(top_two)

#
# def max_ball_students(talabalar):
#     """Eng yaxshi ikkita o'quvchining ismlari va ballarini qaytaruvchi funksiya."""
#
#     # Talabalar lug'atini ballar bo'yicha saralash
#     def get_ball(item):
#         return item[1]
#
#     sorted_students = sorted(talabalar.items(), key=get_ball, reverse=True)
#
#     # Eng yaxshi ikkita o'quvchini olish
#     top_two = sorted_students[:2]
#
#     # Natijani lug'atga aylantirish va qaytarish
#     return dict(top_two)


# Misol
talabalar = {"Akmal": 64, "Tohir": 55, "Nodir": 76, "Zafar": 80}
resultt = max_ball_students(talabalar)
# print(resultt)  # {'Zafar': 80, 'Nodir': 76}

