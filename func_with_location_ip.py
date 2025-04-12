import requests

#Функция возвращает локацию IP
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