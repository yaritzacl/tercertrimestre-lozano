import requests
url="https://ichef.bbci.co.uk/news/800/cpsprodpb/15665/production/_107435678_perro1.jpg"
response=requests.get(url,stream=True)

with open('ope/download.jpg','wb') as file:#creacion de un archivo se crea por medio de un variable y el archivo se itera
    for pedazo in response.iter_content():
        file.write(pedazo)