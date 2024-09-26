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
    gestor.eliminar_tarea(tarea_a_eliminar.identificador())

    assert gestor.cantidad_de_tareas() == 0

def test_se_puede_completar_una_tarea():
    gestor = GestorDeTareas()
    gestor.agregar_tarea("tarea 1")
    tarea_a_completar = gestor.obtener_tareas()[0]
    gestor.marcar_tarea_como_completa(tarea_a_completar.identificador())

    assert tarea_a_completar.completada() is True

def test_se_pueden_completar_multiples_tareas():
    gestor = GestorDeTareas()
    gestor.agregar_tarea("tarea 1")
    gestor.agregar_tarea("tarea 2")
    tarea_a_completar = gestor.obtener_tareas()[0]
    tarea_a_completar1 = gestor.obtener_tareas()[1]
    gestor.marcar_tarea_como_completa(tarea_a_completar.identificador())
    gestor.marcar_tarea_como_completa(tarea_a_completar1.identificador())

    assert tarea_a_completar.completada() is True
    assert tarea_a_completar1.completada() is True

def test_se_puede_marcar_como_incompleta_una_tarea():
    gestor = GestorDeTareas()
    gestor.agregar_tarea("tarea 1")
    tarea = gestor.obtener_tareas()[0]
    gestor.marcar_tarea_como_completa(tarea.identificador())

    assert tarea.completada() is True

    gestor.marcar_tarea_como_incompleta(tarea.identificador())

    assert tarea.completada() is False
