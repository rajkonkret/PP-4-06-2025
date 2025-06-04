# kolekcja

# lista - przechowuje dowolną liczbę elementów, dowolnego typu jednocześnie
# zachowuje kolejność przy dodawaniu elementów

# pusta lista
lista = []
print(lista)  # []

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# append() - dodanie elementów do listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Marek")
lista.append("Kuba")
lista.append("Ela")
lista.append("Anna")
print(lista)
# ['Radek', 'Tomek', 'Zenek', 'Marek', 'Kuba', 'Ela', 'Anna']
#     0        1        2        3        4      5       6
#     -7       -6       -5      -4        -3     -2      -1
# indeksy
print(lista[0])  # Radek
print(lista[2])  # Zenek
print(lista[4])  # Kuba

# print(lista[10])  # IndexError: list index out of range

print(len(lista))  # 7 elementów
print(lista[len(lista) - 1])  # Anna
print(lista[-1])  # Anna, ostatni element z listy
print(lista[-4])  # Marek
print(lista[-7])  # Radek

# # ['Radek', 'Tomek', 'Zenek', 'Marek', 'Kuba', 'Ela', 'Anna']
# slicowanie - fragment listy
print(lista[0:3])  # ['Radek', 'Tomek', 'Zenek'] indeks 012
print(lista[:3])  # ['Radek', 'Tomek', 'Zenek']
print(lista[2:])  # ['Zenek', 'Marek', 'Kuba', 'Ela', 'Anna'], włącznie z ostatnim
print(lista[2:6])  # ['Zenek', 'Marek', 'Kuba', 'Ela'] indeksy 2345, bez 6

print(lista[2:15])  # ['Zenek', 'Marek', 'Kuba', 'Ela', 'Anna']
print(lista[10:234])  # []

print(lista[:])  # ['Radek', 'Tomek', 'Zenek', 'Marek', 'Kuba', 'Ela', 'Anna']
print(lista[2:2])  # []
print(lista[2:3])  # ['Zenek'], indeks 2
print(lista[::2])  # ['Radek', 'Zenek', 'Kuba', 'Anna'] [start:stop:krok], co drugi element

# ['Radek', 'Tomek', 'Zenek', 'Marek', 'Kuba', 'Ela', 'Anna']
#     0        1        2        3        4      5       6
#     -7       -6       -5      -4        -3     -2      -1

print(lista[-2:0])  # [] -> [4:0]
print(lista[0:-2])  # [0:5], ['Radek', 'Tomek', 'Zenek', 'Marek', 'Kuba']

lista_15 = list(range(15))  # od 0 do 14
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(lista_15[::2])  # [0, 2, 4, 6, 8, 10, 12, 14], krok=2

print(lista[::-1])  # w odwrotnej kolejności
# ['Anna', 'Ela', 'Kuba', 'Marek', 'Zenek', 'Tomek', 'Radek']

# nadpisanie elementu
# ['Radek', 'Tomek', 'Zenek', 'Marek', 'Kuba', 'Ela', 'Anna']
lista[3] = "Radek"
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Radek', 'Kuba', 'Ela', 'Anna']

# dopisanie elementu do listy na wskazanym indeksie
lista.insert(1, "Roman")
print(lista)  # ['Radek', 'Roman', 'Tomek', 'Zenek', 'Radek', 'Kuba', 'Ela', 'Anna']

# sprawdzenie indexu dla danego elementu, pierwszy napotkany
print(lista.index("Radek"))  # indeks 0

print(lista.count("Radek"))  # występuje 2 razy

# usunięcie elementu, pierwszy napotkany
lista.remove("Radek")
print(lista)  # ['Roman', 'Tomek', 'Zenek', 'Radek', 'Kuba', 'Ela', 'Anna']

# usunięcie po indeksie, zwraca usunięty element
print(lista.pop(5))  # Ela
print(lista)  # ['Roman', 'Tomek', 'Zenek', 'Radek', 'Kuba', 'Anna']
print(lista.pop(-2))  # Kuba
print(lista.pop())  # Anna, usunie ostatni

a = 1
b = 3
a = b
print(f"{a=}, {b=}")  # a=3, b=3
b = 9
print(f"{a=}, {b=}")  # a=3, b=9

lista2 = lista  # a = b, kopia referencji, adresu
lista_copy = lista.copy()  # kopia elementów listy
print(lista2)  # ['Roman', 'Tomek', 'Zenek', 'Radek']
print(lista)  # ['Roman', 'Tomek', 'Zenek', 'Radek']
lista.clear()  # usunięcie wszystkich eleemntów z listy, krok b = 9
print(lista)  # []
print(lista2)  # []
print(lista_copy)  # ['Roman', 'Tomek', 'Zenek', 'Radek']
print(id(lista))  # 1672499012416
print(id(lista2))  # 1672499012416
print(id(lista_copy))  # 1672501197184

liczby = [54, 999, 34, 22, 12.34, 567]
print(liczby)  # [54, 999, 34, 22, 12.34, 567]
print(type(liczby))  # <class 'list'>

liczby.sort()
print(liczby)  # [12.34, 22, 34, 54, 567, 999], zmiana oryginału
liczby.sort(reverse=True)

liczby = [54, 999, 34, 22, 12.34, 567, "A"]
print(liczby)  # [54, 999, 34, 22, 12.34, 567, 'A']
print(type(liczby))  # <class 'list'>
# liczby.sort() # TypeError: '<' not supported between instances of 'str' and 'int'

lista_copy.reverse()
print(lista_copy)  # ['Radek', 'Zenek', 'Tomek', 'Roman']

# rozpakowanie sekwencji
tekst = "Pyth on."
lista1 = list(tekst)
print(lista1)  # ['P', 'y', 't', 'h', ' ', 'o', 'n', '.']

lista2 = [tekst]
print(lista2)  # ['Pyth on.']

krotka = tuple(lista_copy)
print(type(krotka))  # <class 'tuple'>
print(krotka)  # ('Radek', 'Zenek', 'Tomek', 'Roman')
