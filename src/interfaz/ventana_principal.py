from PySide6.QtWidgets import QMessageBox, QListWidgetItem, QCheckBox
from PySide6.QtCore import Qt
from src.interfaz.ui_tareas import Ui_ListaDeTareas
from src.gestor_de_tareas import GestorDeTareas

class VentanaPrincipal:
    def __init__(self, window):
        self.ui = Ui_ListaDeTareas()
        self.ui.setupUi(window)
        self.gestor = GestorDeTareas()

        self.ui.btnAgregar.clicked.connect(self.agregar_tarea)
        self.ui.btnEliminar.clicked.connect(self.eliminar_tarea)
        self.ui.btnEliminarCompletadas.clicked.connect(self.eliminar_tareas_completadas)

    def agregar_tarea(self):
        descripcion = self.ui.inputDescripcion.text().strip()
        if descripcion:
            self.gestor.agregar_tarea(descripcion)
            self.actualizar_lista()
            self.ui.inputDescripcion.clear()
        else:
            QMessageBox.warning(None, "Error", "La descripción de la tarea no puede estar vacía")

    def eliminar_tarea(self):
        item_seleccionado = self.ui.ListaTareas.currentItem()
        if item_seleccionado:
            tarea_id = item_seleccionado.data(Qt.ItemDataRole.UserRole)
            self.gestor.eliminar_tarea(tarea_id)
            self.actualizar_lista()
        else:
            QMessageBox.warning(None, "Error", "Por favor, seleccione una tarea para eliminar")

    def eliminar_tareas_completadas(self):
        tareas_a_eliminar = [tarea for tarea in self.gestor.obtener_tareas() if tarea.esta_completada()]
        for tarea in tareas_a_eliminar:
            self.gestor.eliminar_tarea(tarea.obtener_identificador())
        self.actualizar_lista()

    def marcar_completada(self, item):
        checkbox = self.ui.ListaTareas.itemWidget(item)
        completada = checkbox.isChecked()
        tarea_id = item.data(Qt.ItemDataRole.UserRole)

        if completada:
            self.gestor.marcar_completada(tarea_id)
        else:
            self.gestor.marcar_incompleta(tarea_id)

        self.actualizar_lista()

    def actualizar_lista(self):
        self.ui.ListaTareas.clear()

        for tarea in self.gestor.obtener_tareas():
            item = QListWidgetItem()
            checkbox = QCheckBox(tarea.obtener_descripcion())
            checkbox.setChecked(tarea.esta_completada())

            checkbox.setFocusPolicy(Qt.FocusPolicy.NoFocus)

            checkbox.stateChanged.connect(lambda estado, item=item: self.marcar_completada(item))

            self.ui.ListaTareas.addItem(item)
            self.ui.ListaTareas.setItemWidget(item, checkbox)

            item.setData(Qt.ItemDataRole.UserRole, tarea.obtener_identificador())
