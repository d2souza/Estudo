import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

#HTML da notícia
noticias = site.find_all('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:
    try:
        titulo = noticia.find('a', attrs={'class': 'feed-post-link'}) # type: ignore
        subtitulo = noticia.find('div', attrs={'class': 'bstn-fd-relatedtext'}) # pyright: ignore[reportCallIssue]
        resumo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'}) # type: ignore
        if subtitulo:
            lista_noticias.append({'titulo': titulo.text, 'link': titulo['href'], 'subtitulo': subtitulo.text}) # type: ignore
        elif resumo:
            lista_noticias.append({'titulo': titulo.text, 'link': titulo['href'], 'subtitulo': resumo.text}) # type: ignore
    except (AttributeError):
        print("Conteúdo não disponível")

news = pd.DataFrame(lista_noticias, columns=['titulo', 'link', 'subtitulo']) 

news.to_csv('noticias.xlsx', index=False)

#print(news)
    
    








