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

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
while 5 in my_list:
    my_list.remove(5)
print(my_list)  # [1, 2, 3, 4, 6] usuniętea liczba 5, niezmieniona kolejnosć

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
print(dict.fromkeys(my_list))
# {1: None, 5: None, 2: None, 3: None, 4: None, 6: None}
unique_numbers = list(dict.fromkeys(my_list))
print(unique_numbers)  # [1, 5, 2, 3, 4, 6] usnięte dulikaty bez z miany kolejności
