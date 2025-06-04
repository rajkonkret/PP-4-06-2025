tekst = "Witaj Świecie"

print(tekst)  # Witaj Świecie
print(type(tekst))  # <class 'str'>

# teksty są niemutowalne
tekst.upper()
""" Return a copy of the string converted to uppercase. """
print(tekst)  # Witaj Świecie
print(tekst.upper())  # WITAJ ŚWIECIE, zwraca kopię
upper_case = tekst.upper()
print(upper_case)  # WITAJ ŚWIECIE
print(tekst)  # Witaj Świecie

print(tekst.capitalize())  # Witaj świecie
print(tekst.lower())  # witaj świecie

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

# strip() - usuwa wiodące i końcowe spacje i białe znaki
print(tekst.removeprefix("Witaj").strip())  # "Świecie"

encoded_s = tekst.encode("utf-8")
print(encoded_s)  # b'Witaj \xc5\x9awiecie' - typ bajtowy
# \xc5\x9a - zapis  w systemie szesnastkowym kodu literki Ś
print(type(encoded_s))  # <class 'bytes'>
print(encoded_s.decode('utf-8'))  # Witaj Świecie

print(tekst)  # Witaj Świecie
# Witaj Świecie
# 01234567890... indeksy od 0

print(tekst[4])  # "j" indeks 4, pozycja 5

print(tekst.count("i"))  # występuje 3 razy
print(tekst.count("j", 0, 4))  # wystapi 0 razy, indeksy 0123 bada

imie = "Radek"
print(imie)  # Radek

print("Imie:", imie)  # Imie: Radek

starszy = "Witaj %s!"  # %s - wstaw w to miejsce str
print(starszy % imie)  # Witaj Radek!

# f - string
tekst_format = f"Mam na imię {imie} i lubię Python"
print(tekst_format)  # Mam na imię Radek i lubię Python

tekst_format = f"\tMam na imię {imie}\n i lubię Pythona.\b"
print(tekst_format)
# \t tabulator
# \n - nowa linia
# \b - backspace
# "	Mam na imię Radek
#  i lubię Pythona"

print("Witaj {}!".format(imie))  # Witaj Radek!

print("""Teskt
    wielolinijkowy""")
# "Teskt
#     wielolinijkowy"

"""Komentarz
wielolinijkowy"""
