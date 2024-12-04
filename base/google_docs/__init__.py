import requests
def get_google_doc_text(doc_url):
    # Преобразование URL для экспорта содержимого в текст
    export_url = doc_url.replace("/edit?usp=sharing", "/export?format=txt")

    # Загрузка содержимого
    response = requests.get(export_url)

    # Проверка успешности запроса
    if response.status_code == 200:
        return response.text
    else:
        return f"Ошибка: не удалось загрузить документ, статус код {response.status_code}"
