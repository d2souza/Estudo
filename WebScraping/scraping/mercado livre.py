import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_produtos = []

url_base = 'https://lista.mercadolivre.com.br/'

produto_buscado = input('Digite o produto que deseja buscar: ')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

response = requests.get(url_base + produto_buscado, headers=headers)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.find_all('div', attrs={'class': 'ui-search-result__content-wrapper'})
if not produtos:
    produtos = site.find_all('div', attrs={'class': 'poly-card__content'})
else:
    print('Produto não encontrado.')
    with open('pagina_erro.html', 'w', encoding='utf-8') as f:
        f.write(site.prettify())  # type: ignore
    print("Verifique o arquivo 'pagina_erro.html' na pasta para entender o que houve.")
for produto in produtos:
    titulo = produto.find('h3', attrs={'class': 'poly-component__title-wrapper'})  # type: ignore

    link = produto.find('a', attrs={'class': 'poly-component__title'})  # type: ignore

    valor = produto.find('div', attrs={'class': 'poly-price__current'})
    simbolo_moeda = valor.find('span', attrs={'class': 'andes-money-amount__currency-symbol'})
    valor_inteiro = valor.find('span', attrs={'class': 'andes-money-amount__fraction'})
    valor_centavos = valor.find('span', attrs={'class': 'andes-money-amount__cents andes-money-amount__cents--superscript-24'})

    if produto:
        lista_produtos.append({'Título': titulo.text, 'Link': link['href'], 'Preço': f"{simbolo_moeda.text}{valor_inteiro.text},{valor_centavos.text if valor_centavos else "00"}"})

produtos_df = pd.DataFrame(lista_produtos, columns=['Título', 'Link', 'Preço'])

produtos_df.to_excel(produto_buscado + '.xlsx', index=False)


