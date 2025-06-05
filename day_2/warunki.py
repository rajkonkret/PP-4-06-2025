# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# if
# w zależności od warunku (True/False) wykona odpowiedni blok programu

odp = True
# odp = False
if odp:
    # wykonany tylko gdy warunek jest True
    print()
    print()
    print("Brawo")
    print()
    print()

print("Dalsza częśc programu")
#
#
# Brawo
#
#
# Dalsza częśc programu

odp = "Radek"
if odp == "Radek":
    print("Nadal Radek")

# Nadal Radek

odp = 0  # -> False, bool(0)
if odp:  # wyrazenie typ boolean
    print("Działa")
else:  # wprzeciwnym przypadku
    print("Zero -> False")
# Zero -> False

a = "Radek"
if len(a) > 3:
    print(f"Długość wynosi {len(a)}, więcej niż 3")
# Długość wynosi 5, więcej niż 3

a = "Radek"
n = len(a)
if n > 3:
    print(f"Długość wynosi {n}, więcej niż 3")
# Długość wynosi 5, więcej niż 3

# walrus operator, operator morsa
if (n := len(a)) > 3:
    print(f"Długość wynosi {n}, więcej niż 3")
# Długość wynosi 5, więcej niż 3

# # kolejnosc ma znaczenie
# podatek = 0
# zarobki = int(input("Podaj zrobki"))
# if zarobki < 10_000:  # do 9999
#     podatek = 0
# elif zarobki < 40_000:  # od 10_000 do 39_999
#     podatek = 0.2
# elif zarobki < 100_000:  # od 40_000
#     podatek = 0.4
# elif zarobki < 40_000:  # od 10_000 do 39_999
#     podatek = 0.2
# else:
#     podatek = 0.9
#
# print(f"Podatek wynosi {podatek * zarobki} pln.")
# # podatek 0.2 dla przedziału 10_000 do 39_999

suma_zam = 150
if suma_zam > 100:
    rabat = 25
else:
    rabat = 0

print("Rabat wynosi:", rabat)  # Rabat wynosi: 25

rabat = 25 if suma_zam > 100 else 0  # operator warunkowy
print("Rabat wynosi:", rabat)  # Rabat wynosi: 25

# napisac test z...
# zadac pytanie
# pobrac odpowiedz
# wypisac czy prawidłowa

punkty = 0
odp = input("podaj datę Chrztu Polski")  # str
if odp == "966":
    print("Dobrze")
    # punkty = punkty + 1
    punkty += 1
else:
    print("Musisz się jescze douczyć")

print("punkty:", punkty)  # punkty: 1

# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1
