# 19- dars


#1. Fuksiya qaytaradigan stringni katta harflarga o'tkazib beradigan dekorator yarating.

def to_uppercase(case_up):
    """Katta harfga o'tkazuvchi decorator funksiya"""
    def text(*args, **kwargs):
        return case_up(*args, **kwargs).upper() if isinstance(case_up(*args, **kwargs), str) else case_up(*args, **kwargs)
    return text

@to_uppercase
def greets(name):
    return f"Hello Mr. {name}!"

# print(greets('abukuii'))

#2. Fuksiya qaytaradigan stringni teskaraisiga aylantirib(reverse)  beradigan dekorator yarating.

def reverse_case(reve):
    """Ham katta harfga ham teskarisiga aylantirib beradigan funksiya (decorator)"""
    def text(*args, **kwargs):
        result = reve(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()[::-1]
        return result
    return text

@reverse_case
def example(name):
    return f"My name is: {name}"

# print(example("Abukuii"))

# 3. Funksiya ishlashi uchun qancha vaqt ketganini hisoblab beradigan dekorator yozing

import time

def exam_time(times):
    def new_time(*args, **kwargs):
        stime = time.time()
        result = times(*args, **kwargs)
        etime = time.time()
        ftime = etime - stime
        return f" Javob {result}, ishlashi uchun ketgan vaqt kechikktirilishlar bilan birgalikda {ftime:.6f} sekund"
    return new_time

@exam_time
def examplet(x, y):
    time.sleep(1)
    return x + y
# print(examplet(500, 100))

# 4. Funksiya necha marta chaqirilganini sanovchi dekorator yozing

def deco_counter(count):
    def print_count(*args, **kwargs):
        nonlocal counter_cal
        counter_cal += 1
        print(f"Funktsiya {counter_cal}- marta chaqirildi")
        result = count(*args, **kwargs)
        return result
    counter_cal = 0
    return print_count

@deco_counter
def example(x, y):
    return x + y

for _ in range(5):
    print(example(10, 20))