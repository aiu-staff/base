
import requests
import yaml

def load_yaml_from_private_github(url, api_key):
    # Преобразуем URL для доступа к "raw" версии
    raw_url = url.replace("github.com", "raw.githubusercontent.com").replace("/blob", "")

    headers = {
        "Authorization": f"Bearer {api_key}"  # Используем токен аутентификации
    }

    try:
        response = requests.get(raw_url, headers=headers)
        response.raise_for_status()  # Проверка на успешность запроса

        return yaml.safe_load(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при загрузке файла: {e}")
        return None
