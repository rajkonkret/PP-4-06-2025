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
