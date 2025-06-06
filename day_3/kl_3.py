from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa Ptak
    """

    def __init__(self, gatunek, szybkosc):
        """
        Metoda inicjalizująca
        :param gatunek:
        :param szybkosc:
        """

        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    """
    Klasa Kura dziedziczy po klasie Ptak
    """

    def __init__(self, gatunek):
        # obowiązkowo musimy wywołać onstruktor z klasy wyższej
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("ko ko ko ko ko")


class Orzel(Ptak):
    """
    Dziedziczy po klasie Ptak
    """

    def wydaj_odglos(self):
        print("Kir kier kirr")

    def polowanie(self):
        print("Tu", self.gatunek, "Rozpoczynam polowanie")


class Sowa(Ptak):
    """
    kala Sowa
    """


# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# kalsa abstrakcyjna, nie mozna tworzyc obiektów tej kalsy
# or1 = Ptak("Orzel", 45)
# or1.latam()  # Tu Orzel Lecę z szybkością 45
#
# kur1 = Ptak("Kura", 0)
# kur1.latam()
# Tu Kura Lecę z szybkością 0

kur2 = Kura("Kura")
kur2.latam()  # Tu Kura Ja nie latam
or2 = Orzel("Orzeł Bielik", 50)
or2.latam()  # Tu Orzeł Bielik Lecę z szybkością 50
kur2.wydaj_odglos()  # ko ko ko ko ko
or2.wydaj_odglos()  # Kir kier kirr

# TypeError: Can't instantiate abstract class Sowa without an implementation for abstract method 'wydaj_odglos'
# sowa = Sowa("Sowa", 20)

# polimorfizm
# obiekty róznych klas  , dziedziczą po wspólnej klasie
# mają wspolne cechy, metody
lista = [kur2, or2]
for c in lista:
    c.wydaj_odglos()
# ko ko ko ko ko
# Kir kier kirr

or2.polowanie()  # Tu Orzeł Bielik Rozpoczynam polowanie
