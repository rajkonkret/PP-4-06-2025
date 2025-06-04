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
