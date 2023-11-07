# utils.py

def calcular_puntuacion(curriculum):
    puntuacion = 0

    # Puntaje basado en años de experiencia
    if curriculum.anios_experiencia >= 5:
        puntuacion += 10
    elif curriculum.anios_experiencia >= 1:
        puntuacion += 5

    # Puntaje basado en habilidades (agregar tus propias condiciones)
    if 'Python' in curriculum.habilidades:
        puntuacion += 5

    # Puntaje basado en idiomas (agregar tus propias condiciones)
    if 'Inglés' in curriculum.idiomas:
        puntuacion += 5

    # Puedes agregar más criterios y ajustar los valores según tus necesidades.

    return puntuacion

