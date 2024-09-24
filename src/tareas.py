class Tarea:
    id_contador = 1

    def __init__(self, descripcion):
        self.__id = Tarea.id_contador
        self.__descripcion = descripcion
        self.__estado = False
        Tarea.id_contador += 1

    def completar(self):
        self.__estado = True

    def revertir(self):
        self.__estado = False

    def mostrar_tarea(self):
        return self.__descripcion

    def esta_completada(self):
        return self.__estado

    def obtener_descripcion(self):
        return self.__descripcion

    def obtener_identificador(self):
        return self.__id

    def __str__(self):
        return f"Tarea(id={self.__id}, descripcion='{self.__descripcion}', completada={self.__estado})"