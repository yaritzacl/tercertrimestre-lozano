from os import strerror
from ejercicio11 import *

counter1 ={char(ch): 0 for ch in range(ord('a'),ord('z')+1)}

try:
    file = open('c:\ya\yaritza.txt', 'rt')
    charater_counter = line_counter
    
    line = file.readline()
    while line != '':
        linea_contar += 1
        for char in line:
            print(char, end='')
            counter1 += 1
        linea = file.readline()
    file.close()
    print("\n\nCaracteres en el archivo:", counter1)
    print("Líneas en el archivo:     ", linea_contar)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))
