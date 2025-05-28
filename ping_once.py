import requests

URLS = [
    'https://calculadorasnauticas.streamlit.app/',
    'https://rectasaltura.streamlit.app/'
]

def ping_urls_once(urls):
    for url in urls:
        try:
            response = requests.get(url)
            print(f"Ping {url}: {response.status_code}")
        except Exception as e:
            print(f"Error ping {url}: {e}")

if __name__ == "__main__":
    ping_urls_once(URLS)
