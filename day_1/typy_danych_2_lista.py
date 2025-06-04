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
