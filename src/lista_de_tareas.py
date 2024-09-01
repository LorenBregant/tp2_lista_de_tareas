class Tarea:
    def __init__(self):
        self.__detalle = []

    def agregar_tarea(self, item):
        self.__agregar_al_detalle(item)

    def cantidad_tareas(self):
        return self.__cantidad_de_tareas()

    def completar_tarea(self, item):
        return self.__marcar_como_completada(item)

    def __agregar_al_detalle(self, item):
        self.__detalle.append({"titulo": item, "completada": False})

    def __cantidad_de_tareas(self):
        return len(self.__detalle)

    def __marcar_como_completada(self, item):
        for tarea in self.__detalle:
            if tarea["titulo"] == item:
                tarea["completada"] = True
                return True
        return False
