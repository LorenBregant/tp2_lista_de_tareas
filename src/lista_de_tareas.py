from src.tareas import Tarea

class ListaDeTareas:
    def __init__(self):
        self.__tareas = []
        self.__indice = 0

    def agregar_tarea(self, descripcion):
        tarea = Tarea(descripcion)
        self.__tareas.append(tarea)

    def obtener_tarea_pendiente(self):
        while self.__indice < len(self.__tareas):
            tarea = self.__tareas[self.__indice]
            if not tarea.esta_completada():
                self.__indice += 1
                return tarea.describir_tarea()
            self.__indice += 1
        return None

    def obtener_todas_las_tareas(self):
        return [(tarea.describir_tarea(), tarea.esta_completada()) for tarea in self.__tareas]

    def completar_tarea(self, descripcion):
        for tarea in self.__tareas:
            if tarea.comparar_descripcion(descripcion):
                tarea.completar()
                return True
        return False

    def eliminar_tarea(self, descripcion):
        for tarea in self.__tareas:
            if tarea.comparar_descripcion(descripcion):
                self.__tareas.remove(tarea)
                return True
        return False

    def eliminar_tareas_completadas(self):
        self.__tareas = [tarea for tarea in self.__tareas if not tarea.esta_completada()]

    def actualizar_tarea(self, descripcion, completada):
        for tarea in self.__tareas:
            if tarea.comparar_descripcion(descripcion):
                if completada:
                    tarea.completar()
                else:
                    tarea.revertir()
                return True
        return False
