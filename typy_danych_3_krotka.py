# krotka, tupla - niemutowalną listę, do odczytu
# pozwala efektywniej zarządzać pamięcią
# stała - zmienna niezmienna

tupla_imiona = ('Radek', "Tomek", "Zenek", "Ela")
print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Ela')
print(type(tupla_imiona))  # <class 'tuple'>

tupla_liczba = 43, 55, 22.34, 11, 200
print(tupla_liczba)  # (43, 55, 22.34, 11, 200)
print(type(tupla_liczba))  # <class 'tuple'>

tupla = 43
print(type(tupla))  # <class 'int'>

tupla2 = 43,
print(type(tupla2))  # <class 'tuple'>
print(tupla2)  # (43,)
print(len(tupla2))  # 1 element

# PEP8 zaleca by tupla jednoelementowa była tworzona  z ()
tupla3 = ("Radek",)
print(type(tupla3))  # <class 'tuple'>
print(tupla3)  # ('Radek',)

# tupla jest niemutowalna
# tupla_liczba[3] = 123  # TypeError: 'tuple' object does not support item assignment

del tupla_liczba
# print(tupla_liczba)  # NameError: name 'tupla_liczba' is not defined

tupla4 = tupla3
print(id(tupla4))  # 2229480702208
print(id(tupla3))  # 2229480702208

del tupla3
print(tupla4)  # ('Radek',)

print(tupla_imiona.index("Radek"))  # index 0
print(tupla_imiona.count("Radek"))  # występuje 1 raz
