string = f"""Radek"""

with open("test.log", "w", encoding="utf-8") as fh:
    fh.write("Powitanie\n")
    fh.write("kolejne\n")
    fh.write("Jescze jedno\n")
    fh.write(f"""Radek
Kowalski""")

with open("test.log", "r", encoding='utf-8') as f:
    data = f.readlines()

print(data)
# ['Powitanie\n', 'kolejne\n', 'Jescze jedno\n', 'Radek\n', 'Kowalski']
for line in data:
    line_data = line.split()
    for l in line_data:
        print(l)
# ['Powitanie\n', 'kolejne\n', 'Jescze jedno\n', 'Radek\n', 'Kowalski']
# Powitanie
# kolejne
# Jescze
# jedno
# Radek
# Kowalski
