#Rekursiv Funksiyalar
# '''Quick Sort - Listni tartiblash uchun '''
from dars14 import result


def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        left = [x for x in lst[1:] if x <= pivot]
        right = [x for x in lst[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)


# print(quick_sort([4, 7, 1, 2, 5, 6, 3]))

# Hanoyi oyini
# '''Hanoi oyini ishlash algoritmi'''
def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        return
    TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod)


# n = int(input("Enter the number of disks"))
# TowerOfHanoi(n, 'A', 'C', 'B')

# 17 dars. Iterator va Generator
# Iterator - iterable ustidagi iteratsiyani boshqaradigan obyektlar
# Iterable - Elementlarning sikla aylantirishga imkoni bor bo'lgan to'plami
# Sequence - Elementlarning qatiy tartiblangan toplami (list, string, dict, tuple)
# Barcha Sequence lar iterable lekin, Barcha iterable lar Sequence emas misol set() index random boladi


# def toq_son_gen():
#     '''Toq sonni ketma ket chiqaruvchi funktsiya'''
#     for i in range(1, 10, 2):
#         n = i
#         yield n
# result1 = toq_son_gen()
# print(next(result1))
# print(next(result1))

# def prime_generator():
#     """"Tub sonni ketma ket chiqaruvchi funktsiya"""
#     def is_prime(number):
#         if number < 2:
#             return False
#         for i in range(2, int(number**0.5) + 1):
#             if number % i == 0:
#                 return False
#         return True
#
#     number = 6
#     while True:
#         if is_prime(number):
#             yield number
#         number += 1
#
# primes = prime_generator()
# for _ in range(6):
#
#     print(next(primes))


# import itertools
#
# def password_generator(input_string):
#     for pwd in itertools.permutations(input_string):
#         yield ''.join(pwd)
#
# input_string = "abs"
# passwords = password_generator(input_string)
# for _ in range(6):
#     print(next(passwords))

# def fibonacci_generator():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# fibonacci = fibonacci_generator()
# for _ in range(10):
#     print(next(fibonacci))


# import itertools
#
# def group_generator(lst, n):
#     for group in itertools.combinations(lst, n):
#         yield group
#
# my_list = [1, 2, 3, 4]
# n = 2
# groups = group_generator(my_list, n)
# for group in groups:
#     print(group)