import requests
from bs4 import BeautifulSoup

url = "https://bank.gov.ua/ua/markets/exchangerates"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')


    exchange_table = soup.find('table', {'class': 'exchange__table'})

    if exchange_table:

        rows = exchange_table.find_all('tr')


        for row in rows[1:]:
            columns = row.find_all('td')
            currency_code = columns[1].text.strip()
            exchange_rate = columns[2].text.strip()

            print(f"Код валюты: {currency_code}, Курс: {exchange_rate}")
    else:
        print("Таблица с курсами валют не найдена на странице.")
else:
    print(f"Не удалось получить страницу. Код состояния: {response.status_code}")
