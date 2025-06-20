# działania z plikami
# filehandler - rura do pliku
# context manager pomaga w pracy z plikami
# with - context manager w pythonie

#    ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open("test.log", "w", encoding="utf-8") as fh:
    fh.write("Powitanie\n")
    fh.write("kolejne\n")
    fh.write("Jescze jedno\n")
    fh.write(f"""Radek
Kowalski""")

# FileExistsError: [Errno 17] File exists: 'test.log'
# x - gdy plik istnieje dostaniemy bład
# with open("test.log", "x") as file:
#     file.write("Powitanie")

# w - nadpisze plik jeśli istnieje
with open("test.log", "w", encoding="utf-8") as f:
    f.write("Nowy\n")

with open("test.log", "a", encoding="utf-8") as fh:
    fh.write("Powitanie\n")
    fh.write("Dodane\n")
    fh.write("dośdane jescze jedno\n")

with open('test.log', "r", encoding='utf-8') as file:
    lines = file.read()

print(lines)
# Nowy
# Powitanie
# Dodane
# dodane jescze jedno
# Nowy
# Powitanie
# Dodane
# dośdane jescze jedno
