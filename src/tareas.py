class Tarea:
    def __init__(self, descripcion):
        self.__descripcion = descripcion
        self.__completada = False

    def completar(self):
        self.__completada = True

    def revertir(self):
        self.__completada = False

    def esta_completada(self):
        return self.__completada

    def comparar_descripcion(self, descripcion):
        return self.__descripcion == descripcion

    def describir_tarea(self):
        return self.__descripcion