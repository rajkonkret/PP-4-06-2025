# while - pętla sterowana warunkiem

# while True:
#     print("Komunikat")

licznik = 0
while True:
    licznik += 1
    print("Komunikat 2 !!")
    if licznik > 10:
        break  # przerywa działanie pętli

print(licznik)  # 11

licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat 3 !!!")
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!

# password = input("Podaj hasło")
# while password != "secret":
#     password = input("Błędne hasło. Podaj ponownie")
#
# print("Hasło prawidłowe")
# Błędne hasło. Podaj ponownieasdasdas
# Błędne hasło. Podaj ponowniesdasfa
# Błędne hasło. Podaj ponownieasdasfsa
# Błędne hasło. Podaj ponownieasasfa``````````````````
# Błędne hasło. Podaj ponowniesecret
# Hasło prawidłowe

lista = []
lista_int = []
while True:
    wej = input("Podaj liczbę")
    # A string is numeric if all characters in the string are numeric
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista_int.append(int(wej))  # rzutujemy na liczbę

print(lista)  # ['1', '2', '3', '4', '5', '6']
print(lista_int)  # [1, 2, 3, 4, 5, 6]
