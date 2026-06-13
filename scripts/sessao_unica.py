from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
import time

sites = [
    "https://globo.com",
    "https://uol.com.br",
    "https://youtube.com",
    "https://twitter.com",
    "https://instagram.com",
    "https://reddit.com",
    "https://terra.com.br",
    "https://folha.uol.com.br",
    "https://cnn.com.br",
    "https://g1.globo.com"
]

options = Options()
options.add_argument("--inprivate")
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)

for site in sites:
    print(f"  Acessando {site}")
    driver.get(site)
    time.sleep(8)

driver.quit()
print("Navegacao concluida.")
