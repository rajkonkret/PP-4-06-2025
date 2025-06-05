# pętla - możliwośc wykonania kodu wielokrotnie
# for - pętla iteracyjna
import random

for i in range(5):  # od 0 do 4
    print(i)

for i in range(5):
    pass  # nic nie rób

for _ in range(5):  # niema zmienna
    print("Test podłoga")
    # print(_)  # 4
# Test podłoga
# Test podłoga
# Test podłoga
# Test podłoga
# Test podłoga

for i in range(10):
    print(i * 2)
    print(i + 2)
# 0
# 2
# 2
# 3
# 4

#
lista_kule = list(range(1, 50))  # od 1 do 49
lista_wynik = []
for _ in range(6):  # od 0 do 5
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    # print(wyn)
    lista_wynik.append(wyn)

print(lista_wynik)  # [27, 23, 8, 43, 14, 13]

for i in range(10):
    if i % 2 == 0:  # modulo
        print(i, "parzysta")

# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

# list comprehensions
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

for c in lista3:  # pobiera po kolei wszystkie lementy z lista3
    if c > 4:
        print(c, "Większe od 4")
    elif c == 4:
        print(c, "Równe 4")
    else:
        print(c, "Mniejsze od 4")
# 0 Mniejsze od 4
# 2 Mniejsze od 4
# 4 Równe 4
# 6 Większe od 4
# 8 Większe od 4

for i in range(0, 10, 2):  # start, stop, krok
    print(i)
# 0
# 2
# 4
# 6
# 8

for i in range(-10, 0):
    print(i)

for i in range(10, 0, -3):  # ujemny krok, idziemy w tył
    print(i)
# 7
# 4
# 1

for c in lista3:
    if c == 2:
        c += 1
        print(c)  # tylko dla c==2
    print("Za każdym przejściem pętli")

print("Po zakońćzeniu pętli")
# Za każdym przejściem pętli
# 3
# Za każdym przejściem pętli
# Za każdym przejściem pętli
# Za każdym przejściem pętli
# Za każdym przejściem pętli
# Po zakońćzeniu pętli

imiona = ["Radek", "Tomek", "Zenek", "Ania"]
print(imiona)  # ['Radek', 'Tomek', 'Zenek', 'Ania']
print(type(imiona))  # <class 'list'>

for p in imiona:
    print(p)
# Radek
# Tomek
# Zenek
# Ania

# 0 Radek
for p in imiona:
    print(imiona.index(p), p)

# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

for i in range(len(imiona)):
    print(i, imiona[i])

# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

# enumerate() - numeruje kolekcje i zwraca numer i element kolekcji
for i in enumerate(imiona):
    print(i)
# (0, 'Radek')
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Ania')
i, o = (3, 'Ania')

for i, o in enumerate(imiona):
    print(i, o)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

for i, o in enumerate(imiona, start=1):
    print(i, o)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Ania

imiona = ["Radek", "Tomek", "Zenek", "Ania"]
wiek = [45, 65, 32, 43]

# Radek 45
for p in imiona:
    print(p, wiek[imiona.index(p)])
# Radek 45
# Tomek 65
# Zenek 32
# Ania 43

# zip() - łączenie kolekcji
for i in zip(imiona, wiek):
    print(i)
# ('Radek', 45)
# ('Tomek', 65)
# ('Zenek', 32)
# ('Ania', 43)

for i, w in zip(imiona, wiek):
    print(i, w)
# Radek 45
# Tomek 65
# Zenek 32
# Ania 43

# 0 Radek 45

for i in enumerate(zip(imiona, wiek)):
    print(i)
# (0, ('Radek', 45))
# (1, ('Tomek', 65))
# (2, ('Zenek', 32))
# (3, ('Ania', 43))
a, b = (0, ('Radek', 45))
print(a, b)  # 0 ('Radek', 45)
c, d = ('Radek', 45)
print(c, d)  # Radek 45
print(a, c, d)
a, (c, d) = (3, ('Ania', 43))
print(a, c, d)  # 3 Ania 43

for i, (o, w) in enumerate(zip(imiona, wiek)):
    print(i, o, w)
# 0 Radek 45
# 1 Tomek 65
# 2 Zenek 32
# 3 Ania 43
