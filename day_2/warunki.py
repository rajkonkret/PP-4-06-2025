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
