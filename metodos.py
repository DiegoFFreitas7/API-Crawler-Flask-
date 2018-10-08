import requests
import asyncio
from bs4 import BeautifulSoup
import functools


async def crawler_Async(lista_url, palavra):
    '''
    Metodo para "enfileirar" a execucao assincrona
    '''
    taks = []
    for url in lista_url:
        taks.append(asyncio.ensure_future(coRotina(url, palavra)))
    await asyncio.gather(*taks)
    return taks


async def coRotina(url, palavra):
    try:
        await asyncio.sleep(0)
        page = requests.get(url)
        resposta = crawler_1(page.content, palavra)
    except:
        await asyncio.sleep(0)
        return {url : -1} # -1 indica que houve erro
    return {url : resposta}


@functools.lru_cache(maxsize=512)
def crawler_1(conteudo, palavra):
    '''
    Metodo que faz a busca de uma 'palavra' no conteudo da TAG 'body' de uma pagina ('url')
    '''
    soup = BeautifulSoup(conteudo, "html.parser")
    body = soup.find_all('body')
    return body[0].get_text().lower().count(palavra.lower())


# Este metodo nao esta sendo utilizado em nenhum lugar
# Esta aqui apenas como uma curiosidade
@functools.lru_cache(maxsize=512)
def crawler_2(conteudo, palavra):
    '''
    Metodo que faz a busca de uma 'palavra' em toda HTML
    '''
    soup = BeautifulSoup(conteudo, "html.parser")
    html = soup.find_all(recursive=False)
    return html[0].get_text().lower().count(palavra.lower())


# Este metodo nao esta sendo utilizado em nenhum lugar
# Esta aqui apenas como uma curiosidade
@functools.lru_cache(maxsize=512)
def crawler_3(conteudo, palavra):
    '''
    Metodo que busca em algumas TAG que contem texto
    '''
    soup = BeautifulSoup(conteudo, "html.parser")
    listaTag = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span', 'a', 'text', 'li', 'td', 'th', 'tr'])
    contador = 0
    # Percorre as principais TAG e conta quantas 'palavras' existem no conteudo delas
    for item in listaTag:
        contador = contador + item.get_text().lower().count(palavra.lower())
    return contador
    

    
    