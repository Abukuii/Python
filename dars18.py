# def f(x):
#     z = 2
#     def g(y): # g hali closure emas
#         return z*x + y
#     return g
# a = 5
# b = 1
# h = f(a) # endi h closure bo'ldi, qaysiki g ga teng bo'lgan.
# print(h(b))  # Output is 11
#
# print(h.__code__.co_freevars) # ('x', 'z')
# # ularning qiymatlari esa:
# print(h.__closure__[0].cell_contents) # 5
# print(h.__closure__[1].cell_contents) # 2

# def f(x):
#     z = 2
#     def g(y):
#         return y
#     return g
# a = 5
# b = 1
# h = f(a)
# print(h(b))  # Output is 1
# print(h.__code__.co_freevars) # Output is ()


# def f(x):
#     def g(y): #closure
#         def h(z): #closure
#             return x * y * z
#         return h
#     return g
# a = 5
# b = 2
# c = 1
# print(f(a)(b)(c))  # Output is 10
#

# def f(x):
#     z = 2
#     return lambda y: z*x+y
# a = 5
# b = 1
# print(f(a)(b))  # Output is 11

def compose(g, f):
    def h(*args, **kwargs): #closure funksiya
        return g(f(*args, **kwargs))
    return h
km_to_m= lambda x: x*1000
m_to_sm= lambda x: x * 100

km_to_sm = compose(m_to_sm, km_to_m)
# print(km_to_sm(12))   # Output 1 200 000

