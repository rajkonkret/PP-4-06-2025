class Car:
    """
    Klasa opisująca samochód w pythonie
    """

    def __init__(self, model, year):
        """
        Metoda inicjalizująca
        :param model:
        :param year:
        """
        self.model = model
        self.year = year
        # pole prywatne, hermetyzacja
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Prędkość wynosi {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10
        self.__zmien_bieg()

    def __zmien_bieg(self):
        print("Zmiana biegu")


# zahermetyzowanie klasy i wystawienie dedykowanych metod do odczytu i zapisu nazywa się enkapsulacją

sam = Car("Wołga", 1963)
sam.gaz()
sam.gaz()
sam.gaz()
sam.gaz()
sam.gaz()
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# pole prywatne
# print(sam.__predkosc)  # 50
sam.licznik()  # Prędkość wynosi 50 km/h
sam.__predkosc = 0  # pole globalne
sam.licznik()  # Prędkość wynosi 50 km/h
sam.hamuj()
sam.hamuj()
sam.hamuj()
sam.hamuj()
sam.hamuj()
sam.licznik()  # Prędkość wynosi 0 km/h
# Prędkość wynosi 50 km/h
# Prędkość wynosi 50 km/h
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Prędkość wynosi 0 km/h
