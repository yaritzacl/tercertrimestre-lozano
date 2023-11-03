import requests
import json

url="https://httpbin.org/post"#?nombre=juan&documento=12345"
argumentos={   #son cabeceras
    'nombre':'Juan',
    'documento':'123'
}

response=requests.post(url,json=argumentos) # al indicarle que en la variable le pasamos ARGUMENTO llamado paramero argumento al momento de la ejecucion no lo muestra en args 
#print(response.content.decode())             #y no muestra en la url sin tener que pasarle los argumentos en ella
decodetest=response.content.decode()          # con el metodo djson response=requests.post(url,djon=argumentos) nos da mas seguridad en la informacion
print(type(decodetest))
print(response.json())
print('*'*20)
decodetestjson=json.loads(response.content)
print(decodetestjson)
print('*'*20)
print(decodetest)

# print(response.content.decode())
# print(type(response.content.decode()))
# jsonresponse=json.loads(response.content)
# print(type(jsonresponse))