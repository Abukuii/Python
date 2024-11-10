# print('hello world')
#
# def ikki_va_uch ():
#     for i in range(1, 40):
#         if i % 2 == 0 and i % 3 == 0:
#             print(f'{i} 2 va 3 ga bo\'linadi')
#
# ikki_va_uch()

import math

example = {
    "yanvar": 12000,
    "fervral": 6000,
    "aprel": 15000,
    "sentabr": 9000,
    "dekabr": 10000,
}
max_sale = max(example.values())
def bigsales(sales):
    for sale in sales:
        if sale == max_sale:
            print(sale)
            for i in range(10):
                if sale == example[i]:
                    print(example.values([i]))


bigsales(example.keys())