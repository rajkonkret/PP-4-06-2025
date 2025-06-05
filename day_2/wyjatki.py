# wyjątek - bład podczas wykonywania programu

# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\PP-4-06-2025\day_2\wyjatki.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero

try:
    # print(5 / 0)
    # print("a" * "23")
    # print(int("A"))
    # raise KeyError("Brak klucza uczniu")  # wygenerowanie błedu
    wynik = 90 / 3
except ZeroDivisionError:
    print("Nie dziel przez zero")
except TypeError:
    print("Blad typu")
except ValueError:
    print("Bład wartości")
except Exception as e:  # worek na pozostałe błędy
    print("Bład:", e)
else:  # tylko gdy nie ma błedu
    print("Wynik działania:", wynik)
finally:
    print("Wykona się zawsze")

print("Działa dalej")
# Nie dziel przez zero
# Działa dalej
# Blad typu
# Działa dalej
# Bład wartości
# Działa dalej
# Bład: 'Brak klucza uczniu'
# Działa dalej
# Wynik działania: 30.0
# Działa dalej
# Wynik działania: 30.0
# Wykona się zawsze
# Działa dalej
