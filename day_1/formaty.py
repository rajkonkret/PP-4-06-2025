import sys

user = "Tomek"  # str
wiek = 30  # int
wersja = 3.900001
print(type(wersja))  # <class 'float'>, zmiennoprzecinkowe
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
#                min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

liczba = 890123456123789  # int

print("Witaj %s masz teraz %d lat." % (user, wiek))  # Witaj Tomek masz teraz 30 lat.
# %d: formatowanie liczb całkowitych
# %f: formatowanie liczb zmiennoprzecinkowych
# %s - łańcuch znaków (string)
# shift ctrl strałka w dół - przesunięcie linii w dół

# TypeError: %d format: a real number is required, not str
# sprawdza typy
# print("Witaj %d masz teraz %s lat." % (user, wiek))  # Witaj Tomek masz teraz 30 lat.

print("Witaj %(imie)s. Jak się czujesz %(imie)s?" % {'imie': user})
# Witaj Tomek. Jak się czujesz Tomek?

print("Witaj {}, masz teraz {} lat.".format(user, wiek))
# Witaj Tomek, masz teraz 30 lat.

print(f"Witaj {user}, masz teraz {wiek} lat.")  # Witaj Tomek, masz teraz 30 lat.

print("Używamy wersji python %i" % 3)  # Używamy wersji python 3
print("Używamy wersji python %f" % 3)  # Używamy wersji python 3.000000
print("Używamy wersji python %.2f" % 3)  # Używamy wersji python 3.00
print("Używamy wersji python %.1f" % 3.9)  # Używamy wersji python 3.9
print("Używamy wersji python %.0f" % 3.9)  # Używamy wersji python 4 - zaokrąglenie
print("Używamy wersji python %.f" % 3.9)  # Używamy wersji python 4 - zaokrąglenie

print(f"Uzywamy wersji {wersja}")  # Uzywamy wersji 3.900001
print(f"Uzywamy wersji {wersja:.2f}")  # Uzywamy wersji 3.90
print(f"Uzywamy wersji {wersja:.1f}")  # Uzywamy wersji 3.9
print(f"Uzywamy wersji {wersja:.0f}")  # Uzywamy wersji 4

print(f"{user:>10}")  # "     Tomek"
print(f"{user:<15}")  # "Tomek          "
print(f"{user:^20}")  # "       Tomek        "

print(len(user))  # długosc sekwencji, 5 znaków
