from os import strerror

try:
    file = open('c:\ya\yaritza.txt','wt')
    
    for i in range(1):
        file.write("Datos personales"+"nombre:camilo"+"edad:23"+"documento:12345445")
        file.close()
except  IOError as e:
    print("se produjo un error ", strerror(e.erno))