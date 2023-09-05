class Pais:
    def __init__(self,nombre,altura,poblacion,eda_me):
        self.__nombre=nombre
        self.__altura=altura
        self.__poblacion=poblacion
        self.__eda_me=eda_me
    def info(self):
        return f"{self.__nombre} {self.__altura} {self.__poblacion} {self.__eda_me}"

    def getNombre(self):
        return self.__nombre

    def getaltura(self):
        return self.__altura

    def getpoblacion(self):
        return self.__poblacion

    def geteda_me(self):
        return self.__eda_me