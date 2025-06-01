from playwright.sync_api import sync_playwright
import time

urls = [
    "https://calculadorasnauticas.streamlit.app/",
    "https://rectasaltura.streamlit.app/"
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    
    for url in urls:
        try:
            print(f"Abriendo {url}")
            page = context.new_page()
            page.goto(url, timeout=30000)
            time.sleep(5)  # Simula permanencia real en la página
            print(f"{url} cargada correctamente")
            page.close()
        except Exception as e:
            print(f"Error accediendo a {url}: {e}")
    
    browser.close()