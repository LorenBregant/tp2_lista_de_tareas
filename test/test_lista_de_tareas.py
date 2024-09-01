from src.lista_de_tareas import Tarea

def test_la_lista_de_tareas_esta_vacia():
    assert Tarea().cantidad_tareas() == 0

def test_se_puede_agregar_una_tarea_a_la_lista():
    tarea = Tarea()
    tarea.agregar_tarea('1')

    assert tarea.cantidad_tareas() == 1

def test_se_pueden_agregar_multiples_tareas_a_la_lista():
    tarea = Tarea()
    tarea.agregar_tarea('1')
    tarea.agregar_tarea('2')

    assert tarea.cantidad_tareas() == 2

def test_se_puede_completar_una_tarea():
    tarea = Tarea()
    tarea.agregar_tarea('comprar pan')

    assert tarea.completar_tarea('comprar pan') is True

def test_se_pueden_completar_varias_tareas():
    tarea = Tarea()
    tarea.agregar_tarea('comprar leche')
    tarea.agregar_tarea('comprar azucar')
    tarea.agregar_tarea('comprar yerba')

    assert tarea.completar_tarea('comprar leche') is True
    assert tarea.completar_tarea('comprar azucar') is True
    assert tarea.completar_tarea('comprar yerba') is True
