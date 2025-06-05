import random

# operacje na liczbach (pseudo)losowych

# """Return random integer in range [a, b], including both end points."""
print(random.randint(1, 100))  # int  od 1 do 100

print(random.randrange(1, 100))  # int od 1 do 99
print(random.randrange(5))  # int od 0 do 4

print(random.random())  # float 0.10920553978758085, od 0 do 0.99999999
print(random.random() * 8)  # float 6.881740583579205, od 0 do 7.99999999

lista = [67, 45, 32, 68, 69, 90, 42]
print(random.choice(lista))  # 42

lista_kule = list(range(1, 50))  # od 1 do 49
# print(lista_kule)

wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)

print(random.choices(lista_kule, k=6))  # [35, 32, 48, 22, 31, 48] z powtórzeniami
print(random.sample(lista_kule, k=6))  # [17, 40, 30, 47, 9, 5]
print(random.sample(lista_kule, 6))  # [36, 44, 42, 20, 30, 17]
