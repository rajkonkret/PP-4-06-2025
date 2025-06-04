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
