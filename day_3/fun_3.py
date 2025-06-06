a = 10  # globalne
b = 10


def dodaj():
    a = 7  # zmienne lokalne, brak wpływu na zmienne o zasięgu globalnym
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)  # przyjmie globalne


def dodaj3():
    global a  # uzyj wewnątrz funkcji globalnej a
    a = 9
    b = 90
    print(a + b)


print(f"Wartość a z góry (globalne): {a=}")  # Wartość a z góry (globalne): a=10
dodaj()  # 15
print(f"Wartość a z góry (globalne): {a=}")  # Wartość a z góry (globalne): a=10
dodaj2()  # 20
print(f"Wartość a z góry (globalne): {a=}")  # Wartość a z góry (globalne): a=10
dodaj3()  # 99
print(f"Wartość a z góry (globalne): {a=}")  # Wartość a z góry (globalne): a=9
dodaj2()  # 19
