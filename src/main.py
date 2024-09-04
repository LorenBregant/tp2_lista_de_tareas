from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from interfaz.ui_tareas import Ui_ListaDeTareas
from src.lista_de_tareas import ListaDeTareas
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ListaDeTareas()
        self.ui.setupUi(self)

        self.lista_de_tareas = ListaDeTareas()

        self.model = QStandardItemModel()
        self.ui.ListaTareas.setModel(self.model)

        self.ui.btnAgregar.clicked.connect(self.agregar_tarea)
        self.ui.btnEliminar.clicked.connect(self.eliminar_tarea)
        self.ui.btnEliminarCompletadas.clicked.connect(self.eliminar_tareas_completadas)

        self.model.itemChanged.connect(self.marcar_completada)

        self.actualizar_lista()

    def agregar_tarea(self):
        descripcion = self.ui.inputDescripcion.text()
        if descripcion:
            self.lista_de_tareas.agregar_tarea(descripcion)
            self.ui.inputDescripcion.clear()
            self.actualizar_lista()

    def actualizar_lista(self):
        self.model.clear()
        for tarea in self.lista_de_tareas.obtener_todas_las_tareas():
            descripcion, completada = tarea
            item = QStandardItem(descripcion)
            item.setCheckable(True)
            item.setCheckState(Qt.CheckState.Checked if completada else Qt.CheckState.Unchecked)
            if completada:
                font = item.font()
                font.setStrikeOut(True)
                item.setFont(font)
            self.model.appendRow(item)

    def marcar_completada(self, item):
        descripcion = item.text()
        completada = item.checkState() == Qt.CheckState.Checked
        self.lista_de_tareas.actualizar_tarea(descripcion, completada)
        self.actualizar_lista()

    def eliminar_tarea(self):
        selected_indexes = self.ui.ListaTareas.selectedIndexes()
        if selected_indexes:
            descripcion = selected_indexes[0].data()
            self.lista_de_tareas.eliminar_tarea(descripcion)
            self.actualizar_lista()

    def eliminar_tareas_completadas(self):
        self.lista_de_tareas.eliminar_tareas_completadas()
        self.actualizar_lista()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
