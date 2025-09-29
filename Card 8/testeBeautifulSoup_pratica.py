from bs4 import BeautifulSoup
import requests

html = requests.get('https://lista.mercadolivre.com.br/notebook#D[A:notebook]')
if html.status_code != 200:
    print(f"Falha ao recuperar a página. Status code: {html.status_code}")
else:
    print("Página recuperada com sucesso!")

soup = BeautifulSoup(html.text, 'lxml')
notebooks = soup.find_all('a', class_='poly-component__title')
print(f"Encontrados {len(notebooks)} notebooks")

for indice, notebook in enumerate(notebooks):
    try:
        link = notebook['href']
        produto = notebook.text.strip()
        print(f'Notebook {indice + 1}:')
        print(f'Produto: {produto}')
        print(f'Link: {link}')
    
        print('')
    except AttributeError as e:
        print(f"Erro ao processar notebook {indice + 1}: {e}")
