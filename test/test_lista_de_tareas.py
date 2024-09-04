from src.lista_de_tareas import ListaDeTareas

def test_se_pueden_agregar_tareas():
    lista = ListaDeTareas()
    lista.agregar_tarea("tarea 1")
    lista.agregar_tarea("tarea 2")
    lista.agregar_tarea("tarea 3")

    assert lista.obtener_tarea() == "tarea 1"
    assert lista.obtener_tarea() == "tarea 2"
    assert lista.obtener_tarea() == "tarea 3"

def test_se_puede_completar_tareas():
    lista = ListaDeTareas()
    lista.agregar_tarea("tarea 1")
    lista.agregar_tarea("tarea 2")
    lista.agregar_tarea("tarea 3")

    assert lista.completar_tarea("tarea 1") is True
    assert lista.completar_tarea("tarea 2") is True
    assert lista.completar_tarea("tarea 3") is True

def test_se_puede_eliminar_tareas():
    lista = ListaDeTareas()
    lista.agregar_tarea("tarea 1")
    lista.eliminar_tarea("tarea 1")

    lista.agregar_tarea("tarea 2")
    lista.eliminar_tarea("tarea 2")

    assert lista.obtener_tarea() is None
