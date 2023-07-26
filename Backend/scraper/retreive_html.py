from bs4 import BeautifulSoup
import re
import requests as req


def get_header(url):
    patron_url = r'https?://(?:www\.)?([a-zA-Z0-9.-]+)\.(?:com|es|net|org)'
    req_url = req.get(url)
    req_url_soup = BeautifulSoup(req_url.text, 'html.parser')
    req_url_soup.find('script').decompose()
    req_url_header = req_url_soup.find('header')
    nombre_dominio_limpio = re.findall(patron_url, url)
    nombre_archivo = '../'+nombre_dominio_limpio[0]+ '.html'
    
    try:
        print('Se ha encontrado el header')
        print(nombre_archivo)
        with open(nombre_archivo, 'w', encoding='utf-8') as file:
            file.write(req_url_header.prettify())
    except:
        print('No se ha encontrado el header')
        try:
            print(req_url_header)
            with open(nombre_archivo, 'w', encoding='utf-8') as file:
                file.write(req_url_header)
        except:
            print(nombre_archivo)
            print(req_url_header)

url = input('Introduce la url: ')
get_header(url)   
