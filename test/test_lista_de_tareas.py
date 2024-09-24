from src.gestor_de_tareas import GestorDeTareas

def test_la_lista_de_tareas_esta_vacia():
    gestor = GestorDeTareas()

    assert gestor.cantidad_de_tareas() == 0

def test_se_puede_agregar_una_tarea():
    gestor = GestorDeTareas()
    gestor.agregar_tarea("tarea 1")

    assert gestor.cantidad_de_tareas() == 1

def test_se_pueden_agregar_multiples_tareas():
    gestor = GestorDeTareas()
    gestor.agregar_tarea("tarea 1")
    gestor.agregar_tarea("tarea 2")

    assert gestor.cantidad_de_tareas() == 2

def test_se_puede_eliminar_una_tarea():
    gestor = GestorDeTareas()
    gestor.agregar_tarea("tarea 1")
    tarea_a_eliminar = gestor.obtener_tareas()[0]
    gestor.eliminar_tarea(tarea_a_eliminar.obtener_identificador())

    assert gestor.cantidad_de_tareas() == 0

def test_se_puede_completar_una_tarea():
    gestor = GestorDeTareas()
    gestor.agregar_tarea("tarea 1")
    tarea_a_completar = gestor.obtener_tareas()[0]
    gestor.marcar_completada(tarea_a_completar.obtener_identificador())

    assert tarea_a_completar.esta_completada() is True

def test_se_pueden_completar_multiples_tareas():
    gestor = GestorDeTareas()
    gestor.agregar_tarea("tarea 1")
    gestor.agregar_tarea("tarea 2")
    tarea_a_completar = gestor.obtener_tareas()[0]
    tarea_a_completar1 = gestor.obtener_tareas()[1]
    gestor.marcar_completada(tarea_a_completar.obtener_identificador())
    gestor.marcar_completada(tarea_a_completar1.obtener_identificador())

    assert tarea_a_completar.esta_completada() is True
    assert tarea_a_completar1.esta_completada() is True

def test_se_puede_marcar_como_incompleta_una_tarea():
    gestor = GestorDeTareas()
    gestor.agregar_tarea("tarea 1")
    tarea = gestor.obtener_tareas()[0]
    gestor.marcar_completada(tarea.obtener_identificador())

    assert tarea.esta_completada() is True

    gestor.marcar_incompleta(tarea.obtener_identificador())

    assert tarea.esta_completada() is False
