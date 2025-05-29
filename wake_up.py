from playwright.sync_api import sync_playwright

urls = [
    "https://calculadorasnauticas.streamlit.app/",
    "https://rectasaltura.streamlit.app/"
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    for url in urls:
        try:
            print(f"Abriendo {url}")
            page.goto(url, timeout=30000)
            print(f"{url} cargada correctamente")
        except Exception as e:
            print(f"Error accediendo a {url}: {e}")
    browser.close()