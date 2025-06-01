import requests

urls = [
    "https://calculadorasnauticas.streamlit.app/",
    "https://rectasaltura.streamlit.app/"
]

for url in urls:
    try:
        print(f"Accediendo a {url}")
        response = requests.get(url, timeout=30)
        print(f"{url} respondió con código {response.status_code}")
    except Exception as e:
        print(f"Error accediendo a {url}: {e}")