# csv - dane oddzielone znakiem podziału ,;tab
# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce
import csv

fields = ['name', 'branch', 'year', 'coe']
row = ['Radek', 'coe', "3", 90]

filename = 'reords.csv'
with open(filename, "w", newline="") as fh:
    csvwriter = csv.writer(fh)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

read_fields = []
read_rows = []

with open(filename, "r", newline="") as f:
    csvreader = csv.reader(f)
    print(csvreader)  # <_csv.reader object at 0x000002504B89C220> iterator

    read_fields = next(csvreader)  # odczyt jedej lini, ustaw odczyt na następną

    for row in csvreader:  # czyta od drugiej lini
        read_rows.append(row)

print("Fields:", read_fields)
print("Rows:", read_rows)
# Fields: ['name', 'branch', 'year', 'coe']
# Rows: [['Radek', 'coe', '3', '90']]
