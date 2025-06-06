# funkcja lambda
# skrócona forma funkcji
# return
from math import lgamma


def odejmij(a, b):
    return a - b


print(odejmij(23, 45))  # -22

odejmij2 = lambda a, b: a - b
print(odejmij2(78, 90))

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

# mapowanie danych
lista = [1, 2, 3, 4, 24, 50, 100, 500]
l = []
for i in lista:
    l.append(i * 2)
print(l)  # [2, 4, 6, 8, 48, 100, 200, 1000]

print([i * 2 for i in lista])  # [2, 4, 6, 8, 48, 100, 200, 1000]


def zmien(x):
    return x * 2


l2 = []
for i in lista:
    l2.append(zmien(i))
print(l2)  # [2, 4, 6, 8, 48, 100, 200, 1000]

# funkcja wyższego rzędu
# map()
print(f"Zastosowanie map: {list(map(zmien, lista))}")  # Zastosowanie map: [2, 4, 6, 8, 48, 100, 200, 1000]
# zastosowanie lambdy jako funkcja anonimowa
# nie ma nazwy
# użycie w miejscu deklaracji
print(f"Zastosowanie map: {list(map(lambda x: x * 2, lista))}")  # Zastosowanie map: [2, 4, 6, 8, 48, 100, 200, 1000]
print(f"Zastosowanie map: {list(map(lambda x: x * 4, lista))}")  # Zastosowanie map: [4, 8, 12, 16, 96, 200, 400, 2000]
print(f"Zastosowanie map: {list(map(lambda x: x * 2.5, lista))}")
# Zastosowanie map: [2.5, 5.0, 7.5, 10.0, 60.0, 125.0, 250.0, 1250.0]

# filtrowanie danych
l3 = []
for i in lista:
    if i < 5:
        l3.append(i)
print(l3)  # [1, 2, 3, 4]

# filter()
print(f"Zastosowanie filter: {list(filter(lambda x: x < 5, lista))}")  # Zastosowanie filter: [1, 2, 3, 4]
print(f"Zastosowanie filter: {list(filter(lambda x: x > 5, lista))}")  # Zastosowanie filter: [24, 50, 100, 500]
print(f"Zastosowanie filter: {list(filter(lambda x: x > 5 and x < 150, lista))}")  # Zastosowanie filter: [24, 50, 100]
print(f"Zastosowanie filter: {list(filter(lambda x: 5 < x < 150, lista))}")  # Zastosowanie filter: [24, 50, 100]
