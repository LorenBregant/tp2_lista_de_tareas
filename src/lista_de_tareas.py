class Tarea:
    def __init__(self):
        self.__detalle = []

    def agregar_tarea(self, item):
        self.__detalle.append(item)

    def cantidad_tareas(self):
        return len(self.__detalle)
