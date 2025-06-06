# klasy - element programowania obiektowego
# klasa - szablon, przepis, opis
# cechy - zmienne
# metody - funkcje
# klasa musi byc zadeklarowana przed użyciem
# tworzenie obiektu uruchmia metode inicjalizującą
# paradygmaty programowania obiektowego
# hermetyzacja, dziedziczenie, polimorfizm i abstrakcja

# PascalCase
class Human:
    """
    Klasa Human w Pythonie
    """

    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print(f"Nazywam się {self.imie}")


print(Human.__doc__)  # Klasa Human w Pythonie
# cd day_3
# pydoc -b - serwer dokumentacji
# pydoc -w kl1 - wygeneruje plik html z dokumentacją klasy

cz1 = Human()
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# None
# k
cz1.imie = "Radek"
cz1.wiek = 45
cz1.plec = "k"

print(cz1.imie)  # Radek
print(cz1.wiek)  # 45
print(cz1.plec)  # k
cz1.powitanie()  # Nazywam się Radek
