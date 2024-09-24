from src.tareas import Tarea

class GestorDeTareas:
    def __init__(self):
        self.__tareas = []

    def agregar_tarea(self, descripcion):
        tarea = Tarea(descripcion)
        self.__tareas.append(tarea)

    def marcar_completada(self, id):
        for tarea in self.__tareas:
            if tarea.obtener_identificador() == id:
                tarea.completar()

    def marcar_incompleta(self, id):
        for tarea in self.__tareas:
            if tarea.obtener_identificador() == id:
                tarea.revertir()

    def eliminar_tarea(self, id):
        for tarea in self.__tareas:
            if tarea.obtener_identificador() == id:
                self.__tareas.remove(tarea)
                break

    def cantidad_de_tareas(self):
        return len(self.__tareas)

    def obtener_tareas(self):
        return self.__tareas
