from src.lista_de_tareas import Tarea

def test_la_lista_de_tareas_esta_vacia():
    assert Tarea().cantidad_tareas() == 0

def test_se_puede_agregar_una_tarea_a_la_lista():
    tarea = Tarea()
    tarea.agregar_tarea('1')

    assert tarea.cantidad_tareas() == 1
