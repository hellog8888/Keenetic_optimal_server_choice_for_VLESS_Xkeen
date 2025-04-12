import requests
import time

# Функция возвращает локацию IP
def get_country_by_ip(ip_address):
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        data = response.json()
        city = data.get("city", "Unknown")
        region = data.get("region", "Unknown")
        country = data.get("country", "Unknown")
        return f"{city}/{region}/{country}"  # Возвращаем код страны (например, "US", "RU")
    except Exception as e:
        print(f"Ошибка при запросе: {e}")
        return "Unknown"


# Преобразуем список хостов в словарь
def ip_and_country_lst_to_dict(file_txt):
    try:
        with open(file_txt, 'r') as file_txt_r:
            res = {k: v for k, v in (line.rstrip('\n').split(':', 1) for line in file_txt_r)}
            return res
    except Exception as e:
        print(f'Ошибка при работе с файлом {e}')


# Создаем словарь IP адрес : Локация
def create_ip_country_dict(lst, dict2):
    ip_country_dict = {}
    dict2 = dict2

    for ip in lst:
        if ip not in dict2:
            country = get_country_by_ip(ip)
            ip_country_dict[ip] = country
            print(f"Добавлен IP: {ip} : {country}")
            time.sleep(1)  # Пауза 1 секунда, чтобы не превысить лимит запросов API

    ip_country_dict = ip_country_dict | dict2
    return ip_country_dict
