import requests

# pip install requests


url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/"
response = requests.get(url)
print(response)  # <Response [200]>
# 200 ok
# 3xx warning
# 4xx 404 - błąd zasobu,
# 5xx - bład po stronie serwera

print(response.text)
# {"table": "A", "currency": "euro", "code": "EUR",
#  "rates": [{"no": "109/A/NBP/2025", "effectiveDate": "2025-06-06", "mid": 4.2881}]}

data = response.json()
print(type(data))  # <class 'dict'>
print(data)
# {'table': 'A', 'currency': 'euro', 'code': 'EUR'
# , 'rates': [{'no': '109/A/NBP/2025', 'effectiveDate': '2025-06-06', 'mid': 4.2881}]}

for k in data:
    print(k)
# table
# currency
# code
# rates

print(data["rates"])  # [{'no': '109/A/NBP/2025', 'effectiveDate': '2025-06-06', 'mid': 4.2881}]
print(data['rates'][0])  # {'no': '109/A/NBP/2025', 'effectiveDate': '2025-06-06', 'mid': 4.2881}
print(data['rates'][0]['mid'])  # 4.2881
