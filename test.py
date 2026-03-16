import requests

try:
    response = requests.get('https://api.telegram.org')
    print("Статус:", response.status_code)
    print("Подключение есть!")
except Exception as e:
    print("Ошибка:", e)