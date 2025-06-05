# słownik - para klucz-wartosc
# {"user" : "Radek"}
# klucze nie mogą sie powtarzac
# odpowiednik jsona

# pusty słownik
dictionary = {}
print(type(dictionary))  # <class 'dict'>
print(dictionary)  # {}

pusty_slownik = dict()
print(type(pusty_slownik))  # <class 'dict'>
print(pusty_slownik)  # {}

# dodanie elementu do słownika
dictionary['imie'] = "Radek"
print(dictionary)
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 67
print(dictionary)  # {'imie': 'Radek', 'wiek': 67}

print(dictionary.keys())  # dict_keys(['imie', 'wiek'])
print(dictionary.values())  # dict_values(['Radek', 67])
print(dictionary.items())  # dict_items([('imie', 'Radek'), ('wiek', 67)])

dict_list = {'imie': ["radek", "Tomek", "Zenek"]}
print(dict_list)  # {'imie': ['radek', 'Tomek', 'Zenek']}

# wypisanie wartosci
print(dictionary['imie'])  # Radek
print(dict_list['imie'])  # ['radek', 'Tomek', 'Zenek'] -> lista
print(dict_list['imie'][2])  # Zenek

# print(dictionary['Imie']) # KeyError: 'Imie'

print(dictionary.get('imie'))  # Radek
print(dictionary.get('Imie'))  # None
print(dictionary.get('Imie', "default"))  # default
print(dictionary.get('imie', "default"))  # Radek

dictionary.update({'data': '31-12-2025'})
print(dictionary)  # {'imie': 'Radek', 'wiek': 67, 'data': '31-12-2025'}

# # input() - pozwala wprowadzić dane do komputera
tekst = input("Podaj imię")
print(tekst)
# # Podaj imięRadek
# # Radek
# ctrl / - komentowanie

# napisac aplikację kalkulator
# pobrac dwie liczby
# wyswietlic wynik obliczenia(+)
# ctrl shift f - wyszuzkiwanie w plikach
