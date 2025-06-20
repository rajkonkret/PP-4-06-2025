wiek = 47  # int
rok = 2025  # int
temp = 36.6  # float

print(wiek + rok)  # 2072
print(wiek - rok)  # -1978
print(wiek * rok)  # 95175
print(wiek / rok)  # 0.023209876543209877 -> float

print(rok // wiek)  # 43, część całkowita z dzielenia 2025 // 47 = 43 całe
print(rok % wiek)  # modulo, reszta z dzielenia 2025 // 47 = 43 całe i reszty 4
# 43 * 47 = 2021 + 4 = 2025
print(10 % 3)  # 1, 3 całe i 1 reszty

print(wiek ** rok)  # potęgowanie
# len() długość sekwencji
print(len(str(wiek ** rok)))  # 3386
# print(len(str(wiek ** rok ** 2)))  # 3386
# ValueError: Exceeds
# the
# limit(4300
# digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit

print(54 - 5 * 43 + 4 / 1 + 4 / 2)  # -155.0
print(54 - 5 * 43 + (4 / 1 + 4) / 2)  # -157.0

# typ float - liczby zmiennoprzecinkowe
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999 błąd zaokrąglenia
# the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345
# decimal - pozwala lepiej zarządzac błędem zaokrąglenia

# typ logiczny
# prawda, fałsz
# True, False
# 1 0

czy_znasz_pythona = True
print(czy_znasz_pythona)  # True
print(type(czy_znasz_pythona))  # <class 'bool'>, boolean, typ logiczny

print(int(True))  # 1
print(int(False))  # 0

# bool() - rzutownaie na typ logiczny
print(bool(1))  # True
print(bool(0))  # False

print(bool(100))  # True
print(bool(-100))  # True
print(bool("Radek"))  # True

print(bool(""))  # False
print(bool(None))  # False, odpowiednik null w innych systemach, nic, nie ma, nie wiem

# and - i
print(True and False)  # False
# Expression    Evaluates to
# True and True    True
# True and False    False
# False and True    False
# False and False    False

# or - lub
# The or Operator’s Truth Table:
#
# Expression    Evaluates to
# True or True    True
# True or False    True
# False or True    True
# False or False    False
print(True or False)  # True

# not - negacja
print(not False)  # True
print(not True)  # False

a = 6
b = 8

print(f"Porównanie {a} > {b} = {a > b}")  # Porównanie 6 > 8 = False
print(f"Porównanie {a} < {b} = {a < b}")  # Porównanie 6 < 8 = True
print(f"Porównanie {a} >= {b} = {a >= b}")  # Porównanie 6 >= 8 = False
print(f"Porównanie {a} <= {b} = {a <= b}")  # Porównanie 6 <= 8 = True
print(f"Porównanie {a >= b = }")  # Porównanie a >= b = False
print(f"Porównanie {a} == {b} = {a == b}")  # == - porównanie, Porównanie 6 == 8 = False
print(f"Porównanie {a} != {b} = {a != b}")  # != - czy rózne, Porównanie 6 != 8 = True
