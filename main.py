import requests


def get_exchange_rate(from_currency, to_currency):
    try:
        # Замените YOUR_API_KEY на ваш ключ API
        api_key = '7c7b0255e81d8fdd33c6e67c'
        url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}'

        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            raise Exception(data.get("error-type", "Не удалось получить курс валют"))

        rates = data['conversion_rates']
        if to_currency not in rates:
            raise Exception(f"Валюта {to_currency} не найдена в ответе API")

        return rates[to_currency]
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    if rate is not None:
        return amount * rate
    else:
        return None


# Пример использования
amount = float(input("Введите количество долларов для того, чтобы перевести их в рубли: "))
from_currency = 'USD'
to_currency = 'RUB'

converted_amount = convert_currency(amount, from_currency, to_currency)
if converted_amount is not None:
    print(f'{amount} {from_currency} = {converted_amount:.2f} {to_currency}')
else:
    print("Конвертация не удалась.")
