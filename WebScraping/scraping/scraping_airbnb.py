import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep

tempo_limite = 10

options = Options()
options.add_argument('window-size=400,800')

navegador = webdriver.Chrome(options=options)

navegador.get('https://www.airbnb.com.br')

sleep(3)
try:
    botao = WebDriverWait(navegador, tempo_limite).until(
        EC.element_to_be_clickable((By.TAG_NAME, 'button'))
    )
    botao.click()
    sleep(2)
    campo_busca = WebDriverWait(navegador, tempo_limite).until(
        EC.element_to_be_clickable((By.ID, 'stays-where-input'))
    )
    campo_busca.click()
    sleep(2)
    campo_busca.send_keys('Penedo')
    sleep(2)
    campo_busca.submit()
    sleep(5)

    botao_avancar = WebDriverWait(navegador, tempo_limite).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text()="24")]'))
    )
    botao_avancar.click()
    sleep(1)
except Exception as e:
    print(f'Não foi possível encontrar o elemento: {e}')



#site = BeautifulSoup(navegador.page_source, 'html.parser')
#print(site.prettify())





