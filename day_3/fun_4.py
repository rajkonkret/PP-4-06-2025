# stworzyć funkcję obliczająćą średnią

def liczby(name=None, *cyfry):  # * - worek na dane
    print(cyfry)
    count = len(cyfry)
    suma = 0
    suma_p = sum(cyfry)
    try:
        for c in cyfry:
            suma += c

        avg = suma / count
        avg_p = suma_p / count
    except Exception as e:
        print("Bład", e)
    else:
        print(f"Średnia dla ucznia {name} wynosi {avg}")
        print(f"Średnia dla ucznia {name} wynosi {avg_p}")
    finally:
        print("Następny")


liczby()  # ()
liczby(1, 2, 3)
liczby(1, 2, 3, 4, 5)
liczby("Radek", 1, 2, 3, 4, 5, 6)
a, *b = ("Radek", 1, 2, 3, 4, 5, 6)
# ()
# Bład division by zero
# Następny
# (1, 2, 3)
# Średnia wynosi 2.0
# Następny
# (1, 2, 3, 4, 5)
# Średnia wynosi 3.0
# Następny
# (1, 2, 3, 4, 5, 6)
# Średnia dla ucznia Radek wynosi 3.5
# Średnia dla ucznia Radek wynosi 3.5
# Następny
