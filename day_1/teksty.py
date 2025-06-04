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
