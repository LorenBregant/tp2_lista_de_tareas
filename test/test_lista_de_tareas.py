from src.lista_de_tareas import ListaDeTareas

def test_se_puede_añadir_una_tarea_a_la_lista():
    lista = ListaDeTareas()
    lista.agregar_tarea("tarea 1")

    assert lista.cantidad_de_tareas() == 1

def test_se_puede_añadir_multiples_tareas():
    lista = ListaDeTareas()
    lista.agregar_tarea("tarea 1")
    lista.agregar_tarea("tarea 2")

    assert lista.cantidad_de_tareas() == 2

def test_se_puede_completar_una_tarea():
    lista = ListaDeTareas()
    lista.agregar_tarea("tarea 1")

    assert lista.completar("tarea 1") == "Completada"

def test_se_puede_completar_multiples_tareas():
    lista = ListaDeTareas()
    lista.agregar_tarea("tarea 1")
    lista.agregar_tarea("tarea 2")

    assert lista.completar("tarea 1") == "Completada"
    assert lista.completar("tarea 2") == "Completada"

# def test_se_puede_completar_tareas():
#     lista = ListaDeTareas()
#     lista.agregar_tarea("tarea 1")
#     lista.agregar_tarea("tarea 2")
#     lista.agregar_tarea("tarea 3")
#
#     assert lista.completar_tarea("tarea 1") == True
#     assert lista.completar_tarea("tarea 2") == True
#     assert lista.completar_tarea("tarea 3") == True
#
# def test_se_puede_eliminar_tareas():
#     lista = ListaDeTareas()
#     lista.agregar_tarea("tarea 1")
#     lista.eliminar_tarea("tarea 1")
#
#     lista.agregar_tarea("tarea 2")
#     lista.eliminar_tarea("tarea 2")
#
#     assert lista.obtener_tarea_pendiente() is None
