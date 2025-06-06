# funkcja zwracająca wynik
# return

def dodaj(a, b):
    return a + b


def odejmij(a=0, b=0, c=0):
    return a - b - c


print(dodaj(5, 90))  # 95
print(odejmij())  # 0
print(odejmij(5, 7, 9))  # -11

zm = odejmij(45, 10, 2)
print("Wynik:", zm)  # Wynik: 33
