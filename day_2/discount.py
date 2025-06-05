from datetime import datetime, date, timedelta

today = date.today()
print("Dzisiejsza data:", today)  # Dzisiejsza data: 2025-06-05
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print("Aktualna godzina:", time)  # Aktualna godzina: 2025-06-05 14:53:19.767772
print(type(time))  # <class 'datetime.datetime'>

print(time.year)  # 2025
print(today.day)  # 5

# tomorrow = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print("Jutro będzie:", tomorrow)  # Jutro będzie: 2025-06-06
print(type(tomorrow))  # <class 'datetime.date'>

formated_date = datetime.now().strftime("%d/%m/%Y")
print("Sformatowana data:", formated_date)  # Sformatowana data: 05/06/2025
print(type(formated_date))  # <class 'str'>

# 15:00
formated_time = datetime.now().strftime("%H:%M")
print("Aktualna godzina:", formated_time)  # Aktualna godzina: 15:02
print(type(formated_time))  # <class 'str'>

formated_time_12_h = datetime.now().strftime("%I:%M %p")
print("Godzina w formacie 12h:", formated_time_12_h)  # Godzina w formacie 12h: 03:03 PM
print("Godzina w formacie 12h:", formated_time_12_h.removeprefix("0"))  # Godzina w formacie 12h: 3:05 PM

object_datetime = datetime.now().strptime("05/06/2025", "%d/%M/%Y")
print("Obiekt date ze stringa:", object_datetime)  # Obiekt date ze stringa: 2025-01-05 00:06:00
print(type(object_datetime))  # <class 'datetime.datetime'>


