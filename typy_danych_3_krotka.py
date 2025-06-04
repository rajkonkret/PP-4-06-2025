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

# ropzakownie tupli
tup = 1, 2
print(type(tup))  # <class 'tuple'>

a, b = 1, 2
print(a, b)  # 1 2

a, b = tup
print(a, b)  # 1 2

tup2 = 1, 2, 3
# a, b = tup2  # ValueError: too many values to unpack (expected 2)
a, *b = tup2  # * worek na pozostałe dane
print(a, b)  # 1 [2, 3]

tupla_imiona = ('Radek', "Tomek", "Zenek", "Ela")
name1, name2, *name3 = tupla_imiona
print(f"{name1=}, {name2=}, {name3=}")  # name1='Radek', name2='Tomek', name3=['Zenek', 'Ela']

name1, *name2, name3 = tupla_imiona
print(f"{name1=}, {name2=}, {name3=}")  # name1='Radek', name2=['Tomek', 'Zenek'], name3='Ela'

*name1, name2, name3 = tupla_imiona
print(f"{name1=}, {name2=}, {name3=}")  # name1=['Radek', 'Tomek'], name2='Zenek', name3='Ela'

# zwróci posortowaną listę
print(sorted(tupla_imiona))  # ['Ela', 'Radek', 'Tomek', 'Zenek']
print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Ela') krotka się nie zmieni

lista_z_tupli = list(tupla_imiona)
print(lista_z_tupli)  # ['Radek', 'Tomek', 'Zenek', 'Ela']
print(type(lista_z_tupli))  # <class 'list'>
