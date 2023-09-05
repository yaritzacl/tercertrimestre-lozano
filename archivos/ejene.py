from os import strerror

try:
    315
    flujo= open('C:\ya\\prueba.txt','r',encoding='utf-8')
    linea=flujo.readlines()
    print (flujo.linea)
except IOError:
    print("escriba bien")