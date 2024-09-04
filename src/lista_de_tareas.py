from src.tareas import Tarea

class ListaDeTareas:
    def __init__(self):
        self.__tareas = []

    def agregar_tarea(self, descripcion):
        tarea = Tarea(descripcion)
        self.__tareas.append(tarea)

    def obtener_tarea_pendiente(self):
        for tarea in self.__tareas:
            if not tarea.completada:
                return tarea.descripcion
        return None

    def obtener_todas_las_tareas(self):
        return [(tarea.descripcion, tarea.completada) for tarea in self.__tareas]

    def completar_tarea(self, descripcion):
        for tarea in self.__tareas:
            if tarea.descripcion == descripcion:
                tarea.completar()
                return True
        return False

    def eliminar_tarea(self, descripcion):
        for tarea in self.__tareas:
            if tarea.descripcion == descripcion:
                self.__tareas.remove(tarea)
                return True
        return False

    def eliminar_tareas_completadas(self):
        self.__tareas = [tarea for tarea in self.__tareas if not tarea.completada]

    def actualizar_tarea(self, descripcion, completada):
        for tarea in self.__tareas:
            if tarea.descripcion == descripcion:
                if completada:
                    tarea.completar()
                else:
                    tarea.revertir()
                return True
        return False
