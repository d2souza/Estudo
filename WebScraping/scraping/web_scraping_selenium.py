from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

tempo_limite = 10
navegador = webdriver.Chrome()

navegador.get('https://www.kaggle.com/datasets')

try:
    campo_busca = WebDriverWait(navegador, tempo_limite).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="text" and @placeholder="Search datasets"]'))
    )
    print('Campo de busca encontrado com sucesso!')
    campo_busca.click()
    campo_busca.send_keys('Spotify')
    input('Pressione Enter para continuar...')

except Exception as e:
    print(f'Não foi possível encontrar o campo de busca: {e}')


