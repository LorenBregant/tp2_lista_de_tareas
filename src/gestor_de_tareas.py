#Reglas de negocio
#Se puede agregar una o multiples tareas
#Se puede marcar como completada una o mulltiples tareas
#Se pueden eliminar tareas
from tareas import Tarea


# from src.tareas import Tarea

class ListaDeTareas:
    def __init__(self):
        self.__tareas = []

    def agregar_tarea(self, descripcion):
            self.__tareas.append(descripcion)

    def cantidad_de_tareas(self):
        return len(self.__tareas)

    # def completar(self, tarea):
    #     for item in self.__detalle:
    #         if item["nombre"] == tarea:
    #             item["estado"] = True
    #             return "Completada"

    def mostrar_tareas(self):
        for tarea in self.__tareas:
            print(tarea)

lista = ListaDeTareas()
lista.agregar_tarea("tarea 1")
lista.agregar_tarea("tarea 2")
lista.agregar_tarea("tarea 3")
# lista.completar("tarea 1")
# lista.completar("tarea 2")

lista.mostrar_tareas()
print(lista.cantidad_de_tareas())

# class ListaDeTareas:
#     def __init__(self):
#         self.__tareas = []
#         self.__indice = 0
#
#     def agregar_tarea(self, descripcion):
#         tarea = Tarea(descripcion)
#         self.__tareas.append(tarea)
#
#     def obtener_tarea_pendiente(self):
#         while self.__indice < len(self.__tareas):
#             tarea = self.__tareas[self.__indice]
#             if not tarea.esta_completada():
#                 self.__indice += 1
#                 return tarea.describir_tarea()
#             self.__indice += 1
#         return None
#
#     def obtener_todas_las_tareas(self):
#         return [(tarea.describir_tarea(), tarea.esta_completada()) for tarea in self.__tareas]
#
#     def completar_tarea(self, descripcion):
#         for tarea in self.__tareas:
#             if tarea.comparar_descripcion(descripcion):
#                 tarea.completar()
#                 return True
#         return False
#
#     def eliminar_tarea(self, descripcion):
#         for tarea in self.__tareas:
#             if tarea.comparar_descripcion(descripcion):
#                 self.__tareas.remove(tarea)
#                 return True
#         return False
#
#     def eliminar_tareas_completadas(self):
#         self.__tareas = [tarea for tarea in self.__tareas if not tarea.esta_completada()]
#
#     def actualizar_tarea(self, descripcion, completada):
#         for tarea in self.__tareas:
#             if tarea.comparar_descripcion(descripcion):
#                 if completada:
#                     tarea.completar()
#                 else:
#                     tarea.revertir()
#                 return True
#         return False
