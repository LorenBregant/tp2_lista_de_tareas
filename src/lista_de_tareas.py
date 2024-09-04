class ListaDeTareas:
    def __init__(self):
        self.__tareas = []
        self.__indice = 0

    def agregar_tarea(self, tarea):
        self.__tareas.append(tarea)

    def obtener_tarea(self):
        if self.__indice < len(self.__tareas):
            tarea = self.__tareas[self.__indice]
            self.__indice += 1
            return tarea

    def completar_tarea(self, tarea):
        for item in self.__tareas:
            if item == tarea:
                return True

    def eliminar_tarea(self, tarea):
        for item in self.__tareas:
            if item == tarea:
                self.__tareas.remove(item)
