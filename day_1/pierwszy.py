# PEP8
# ctrl alt l - formatowanie kodu wg zasad PEP8
import sys

print()  # wypisz/wydrukuj pustą linię

print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
# ctrl d - powielanie linii
print('Nazywam się Radek')  # Nazywam się Radek

# print('Radek") # SyntaxError: unterminated string literal (detected at line 13)

# type() - sprawdzenie typu danych
print(type("Radek"))  # <class 'str'>, tekstowe, string

print("39")
print("39" + "39")  # konkatenacja 3939, łaczy stringi

print(39)
print(type(39))  # <class 'int'>, liczby calkowite
print(39 + 39)  # 78

# int() - rzutowanie na int
print(int("39") + int("39"))  # 78

# str() - rzutowanie na tekst
print(str(39) + str(39))  # 3939

# print("39" + 39)  # TypeError: can only concatenate str (not "int") to str
print(int("39") + 39)  # 78

print(168 * 35)  # 5880
print("168" * 35)  # 5880
# 168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168
print(10 * "-")  # ----------

print(sys.int_info)
# sys.int_info(bits_per_digit=30,
#              sizeof_digit=4,
#              default_max_str_digits=4300,
#              str_digits_check_threshold=640)

# zmienna - pudełko na dane, posiada nazwę
# nazwa zmiennej powinna podpowiadac co zawiera
# snake_case - konwencja nazewnicza
# ctrl / - komentowanie zaznaczonej linii

# typowanie dynamiczne - w każdej chwili dowolny typ danych możemy wrzucić do zmiennej
name = "Radek"
print(name)  # Radek, wypisanie wartości zmiennej
print(type(name))  # <class 'str'>

name = 90
print(type(name))  # <class 'int'>
print(name)  # 90

# to są tylko podpowiedzi
name: str = "Radek"
print(name)
print(type(name))

name = 90
print(name)  # 90
print(type(name))  # <class 'int'>
# mypy
