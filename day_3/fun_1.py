# funkcja - wydzielony fragment kodu. można wywołąc w dowolnym momencie
# funkcja musi być najpierw zadekalrowana
# zeby uruchomić funkcję musi zostać wywołana

a = 8
b = 6


# funkcje niezwracające wyniku
# deklaracja funkcji
# PEP8 zaleca aby oddziellic funkcje od programu dwoma pustymi linijkami
def dodaj():  # nie posiada argumentów
    print(a + b)


def dodaj2(a, b):  # obowiązkowe argumenty do przekazania
    # lokalne zmienne a i b
    # inne od globalnych
    print(a + b)  # 134


def odejmij(a, b, c=0):  # argument c ma wartość domyślną
    print(a - b - c)


print("Poza funkcją")

# wywołanie funkcji

# po pozycji
dodaj()  # 14
dodaj2(56, 78)
dodaj2(a, b)
# dodaj2() # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
odejmij(1, 2)  # -1
odejmij(1, 2, 9)  # -10

# po nazwie
odejmij(b=10, c=9, a=67)
dodaj2(b=9, a=7)  # 16

# mieszane
odejmij(1, 2, c=8)  # -9

# pozycyjne muszą byc przed nazwanymi. to wygeneruje bład
# odejmij(a=9, 3,4) # SyntaxError: positional argument follows keyword argument

# print(dodaj() + dodaj()) # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

print(print())  # None
