# 29 talik topshiriq


#1
# a = int(input("Sonni kiriting? >>> "))
# if a < 0: print("Bu son manfiy")
# else: print("Bu son musbat")

#2
# a = int(input("Sonni kiriting? >>> "))
# if a % 2 != 0: print("Bu Toq son")
# else: print("Bu Juft son")

#3
# bir = "Dushanba"
# ikki = "Seshanba"
# uch = "Chorshanba"
# tort = "Payshanba"
# besh = "Juma"
# olti = "Shanba"
# yetti = "Yakshanba"
# ish = "Ish kuni"
# dam = "Dam olish kuni"
#
# haftkuni = int(input("Bugun haftaning nechinchi kuni? >>> "))
#
# if haftkuni == 1:
#     print(f"Bugun {bir}, {ish}")
# elif haftkuni == 2:
#     print(f"Bugun {ikki}, {ish}")
# elif haftkuni == 3:
#     print(f"Bugun {uch}, {ish}")
# elif haftkuni == 4:
#     print(f"Bugun {tort}, {ish}")
# elif haftkuni == 5:
#     print(f"Bugun {besh}, {ish}")
# elif haftkuni == 6:
#     print(f"Bugun {olti}, {dam}")
# elif haftkuni == 7:
#     print(f"Bugun {yetti}, {dam}")
# else:
#     print("Error! Bunday ish kuni mavjud emas!...")

#4
# a = int(input("Sonni kiriting? >>> "))
# if a > 0: print(a + 2)
# else: print(a - 2)

#5
# A = int(input("A ni kiriting? >>> "))
# B = int(input("B ni kiriting? >>> "))
#
# if A > 3 and B <= 6: print(True)
# else: print(False)

#6
# A = int(input("A ni kiriting? >>> "))
# B = int(input("B ni kiriting? >>> "))
#
# if A < 2 and B >= -2: print(True)
# else: print(False)

#7
# A = int(input("A ni kiriting? >>> "))
# B = int(input("B ni kiriting? >>> "))
#
# if A > B: print(A)
# else: print(B)
# if A < B: print(A)
# else: print(B)

#8
# A = float(input("A ni kiriting? >>> "))
# B = float(input("B ni kiriting? >>> "))
#
# e = A % 1
# b = B % 1
#
# if e > b: print(b)
# else: print(e)

#9
# e = int(input("A ni kiriting >>> "))
# b = int(input("B ni kiriting >>> "))
# c = int(input("C ni kiriting >>> "))
#
# if e < b < c: print(True)
# else: print(False)

#10
# e = int(input("A ni kiriting >>> "))
# b = int(input("B ni kiriting >>> "))
# c = int(input("C ni kiriting >>> "))
#
# if e < b < c or c < b < e: print(True)
# else: print(False)

#11
# e = int(input("A ni kiriting >>> "))
# b = int(input("B ni kiriting >>> "))
# c = int(input("C ni kiriting >>> "))
#
# if e > 0 and b > 0 and c > 0: print("3 ta musbat")
# elif e > 0 and b > 0 and c < 0 or e > 0 and b < 0 and c > 0 or e < 0 and b > 0 and c > 0: print("2 ta musbat")
# elif e > 0 and b < 0 and c < 0 or e < 0 and b > 0 and c < 0 or e < 0 and b < 0 and c > 0: print("1 ta musba")
# else: print("musbat yoq")

#12
# e = int(input("A ni kiriting >>> "))
# b = int(input("B ni kiriting >>> "))
# c = int(input("C ni kiriting >>> "))
#
# if e < b < c or e < c < b: print(f"Eng katta lari C va B yigindisi {c + b}")
# elif b < e < c or b < c < e: print(f"Eng katta lari A va C yigindisi {e + c}")
# else: print(f"Eng katta lari A va B yigindisi {e + b}")

#13
# import math
#
# son = int(input("son: "))
#
# chegara = int(math.sqrt(son))
#
# for i in range(2,chegara+1):
#     if son % i == 0:
#         print("tub son emas")
#         break
# else:
#     print("tub son!")

# 14
# e = int(input("A sonini kiriting >>> "))
# b = int(input("B sonini kiriting >>> "))
#
# if e % 2 != 0 and b % 2 != 0:
#     print("2 si ham Toq")

#15
# e = int(input("A sonini kiriting >>> "))
# b = int(input("B sonini kiriting >>> "))
#
# if e % 2 != 0: print("A Toq")
# else: print("A Juft")
# if b % 2 != 0: print("B Toq")
# else: print("B Juft")

#16
# e = int(input("A sonini kiriting >>> "))
# b = int(input("B sonini kiriting >>> "))
# c = int(input("C sonini kiriting >>> "))
#
# if e > 0 and b > 0 and c > 0: print("Musbat")

#17
# e = int(input("Sonni kiriting >>> "))
#
# if e % 2 == 0 and len(str(e)) == 2: print(" son 2 xonali va juft")

#18
# e = int(input("Sonni kiriting >>> "))
#
# if e % 2 != 0 and len(str(e)) == 3: print(" son 3 xonali va toq")

#19
# e = int(input("3 xonali son kiriting >>> "))
# m = e // 100
# n = ( e // 10 ) % 10
# o = e % 10
#
# if m == n == o: print("Sonlar bir xil")

#20
# e = int(input("Sonni kiriting >>> "))
#
# if e > 0: print(f"Son musbat va u {len(str(e))} xonali")
# else: print(f"Son manfiy va u {len(str(abs(e)))} xonali")

#21
# e = int(input("3 xonali sonni kiriting >>> "))
# m = e // 100
# n = ( e // 10 ) % 10
# o = e % 10
#
# if m > n > o: print("Kamayish tartibida")
# elif o > n > m: print("O'sish Tartibida")
# else: print("Aralash tartibda")

#22
# e = int(input("4 xonali sonni kiriting >>> "))
# chap = e // 1000
# chapikki = (e // 100) % 10
# ongikki = ( e // 10 ) % 10
# ong = e % 10
#
# if chap == chapikki == ongikki == ong or chap == ong and chapikki == ongikki:
#     print("Bir xil o'qiladi")

#23
# x = int(input("X ni kiriting >>> "))
# y = int(input("Y ni kiriting >>> "))
#
# if x == 0 and y == 0: print("Kordinata boshi")
# elif x > 0 and y > 0: print("I - chorak")
# elif x < 0 and y > 0: print("II - chorak")
# elif x < 0 and y < 0: print("III - chorak")
# else: print("IV - chorak")

#24
# x1 = int(input("X1 ni kiriting >>> "))
# y1 = int(input("Y1 ni kiriting >>> "))
#
# if (x1 + y1) % 2 != 0: print("Oq rang")
# else: print("Qora rangda")


#25
# x1 = int(input("X1 ni kiriting >>> "))
# y1 = int(input("Y1 ni kiriting >>> "))
# x2 = int(input("X2 ni kiriting >>> "))
# y2 = int(input("Y2 ni kiriting >>> "))
# bir = (x1 + y1) % 2
# ikki = (x2 + y2) % 2
#
# if bir == ikki: print("Bir xil rangda")
# else: print("Bir xil emas")

#26
# x1 = int(input("X1 ni kiriting >>> "))
# y1 = int(input("Y1 ni kiriting >>> "))
# x2 = int(input("X2 ni kiriting >>> "))
# y2 = int(input("Y2 ni kiriting >>> "))
# x = abs(x1 - x2)
# y = abs(y1 - y2)
#
# if x == 0 and y == 1 or x == 1 and y == 0 or x == y:
#     print("Yura oladi")
# else: print("Yura olmaydi")

#27
# x1 = int(input("X1 ni kiriting >>> "))
# y1 = int(input("Y1 ni kiriting >>> "))
# x2 = int(input("X2 ni kiriting >>> "))
# y2 = int(input("Y2 ni kiriting >>> "))
# x = abs(x1 - x2)
# y = abs(y1 - y2)
# if x == y: print("Yura oladi")
# else: print("Yura olmaydi")

#28
# x1 = int(input("X1 ni kiriting >>> "))
# y1 = int(input("Y1 ni kiriting >>> "))
# x2 = int(input("X2 ni kiriting >>> "))
# y2 = int(input("Y2 ni kiriting >>> "))
# x = abs(x1 - x2)
# y = abs(y1 - y2)
#
# if x == y or x == 0 or y == 0:
#     print("Yura oladi")
# else: print("Yura olmaydi")

#29
# n = int(input("1 - yanvar haftaning nechinchi kuni ekanligini yozing? >>> "))
# k = int(input("Haftaning qaysi kuni bo'lishini bilmoqchi bo'lgan sanangizni yozing >>> "))
#
# kun = k % 7 + (n - 1)
#
# if kun == 1: print("Dushanba")
# elif kun == 2: print("Seshanba")
# elif kun == 3: print("Chorshanba")
# elif kun == 4: print("Payshanba")
# elif kun == 5: print("Juma")
# elif kun == 6: print("Shanba")
# elif kun == 7: print("Yakshanba")


# Otabek Nematov