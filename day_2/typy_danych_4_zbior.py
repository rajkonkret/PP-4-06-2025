# zbior (set) -  przechowuje unikalne wartości
# nie achowuje kolejności przy dodawaniu elementów
# nie posiada indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
print(type(zbior))  # <class 'set'>

# pusty zbior
zb2 = set()
print(type(zb2))
print(zb2)  # set()

# dodanie lementów do zbioru
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(24)
zbior.add(32)
zbior.add(17)
print(zbior)  # {32, 33, 66, 777, 11, 44, 17, 18, 22, 55, 24}

# usunięcie lementu zbioru
zbior.remove(55)
print(zbior)  # {32, 33, 66, 777, 11, 44, 17, 18, 22, 24}

# pop() - usunięcie pierwszego elementu ze zbioru
print(zbior.pop())  # 32

zmienna = zbior.pop()
print("Usunięty:", zmienna)  # Usunięty: 33

zbior_copy = zbior.copy()
print(zbior)  # {66, 777, 11, 44, 17, 18, 22, 24}
print(zbior_copy)  # {66, 777, 11, 44, 17, 18, 22, 24}
print(id(zbior))  # 2680093377696
print(id(zbior_copy))  # 2680093678880

