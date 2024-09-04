from src.lista_de_tareas import ListaDeTareas

def test_se_pueden_agregar_tareas():
    lista = ListaDeTareas()
    lista.agregar_tarea("tarea 1")
    lista.agregar_tarea("tarea 2")
    lista.agregar_tarea("tarea 3")

    assert lista.obtener_tarea_pendiente() == "tarea 1"
    assert lista.obtener_tarea_pendiente() == "tarea 2"
    assert lista.obtener_tarea_pendiente() == "tarea 3"

def test_se_puede_completar_tareas():
    lista = ListaDeTareas()
    lista.agregar_tarea("tarea 1")
    lista.agregar_tarea("tarea 2")
    lista.agregar_tarea("tarea 3")

    assert lista.completar_tarea("tarea 1") == True
    assert lista.completar_tarea("tarea 2") == True
    assert lista.completar_tarea("tarea 3") == True

def test_se_puede_eliminar_tareas():
    lista = ListaDeTareas()
    lista.agregar_tarea("tarea 1")
    lista.eliminar_tarea("tarea 1")

    lista.agregar_tarea("tarea 2")
    lista.eliminar_tarea("tarea 2")

    assert lista.obtener_tarea_pendiente() is None
