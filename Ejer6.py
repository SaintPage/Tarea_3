""" ----------------
-------------------------------------------------------------
ÁNGEL DE JESÚS MÉRIDA JIMÉNEZ - 23661
UNIVERSIDAD DEL VALLE DE GUATEMALA
FACULTAD DE MATEMÁTICA 
DEPARTAMENTO DE CIENCIA DE LA COMPUTACIÓN
MATEMÁTICA DISCRETA 1


Actividad: Tarea 3 ejercicio 6
-------------------------------------------------------------
-----------------/"""

def validar_entradas(m, a, c, s, n):
    # Verifica que todas las entradas sean enteros
    if not all(isinstance(i, int) for i in [m, a, c, s, n]):
        raise ValueError("Todos los valores deben ser enteros.")
    
    # Verifica que el multiplicador 'a' cumpla con la condición 2 <= a < m
    if not (2 <= a < m):
        raise ValueError("El multiplicador 'a' debe cumplir con la condición: 2 <= a < m.")
    
    # Verifica que el incremento 'c' cumpla con la condición 0 <= c < m
    if not (0 <= c < m):
        raise ValueError("El incremento 'c' debe cumplir con la condición: 0 <= c < m.")
    
    # Verifica que la semilla 's' cumpla con la condición 0 <= s < m
    if not (0 <= s < m):
        raise ValueError("La semilla 's' debe cumplir con la condición: 0 <= s < m.")
    
    # Verifica que el número de valores a generar 'n' sea un entero positivo
    if n <= 0:
        raise ValueError("El número de valores a generar 'n' debe ser un entero positivo.")

def generar_pseudoaleatorios(m, a, c, s, n):
    # Validar las entradas antes de continuar
    validar_entradas(m, a, c, s, n)
    
    # Inicializar la lista con el valor de la semilla
    pseudoaleatorios = [s]
    
    # Generar 'n' números pseudoaleatorios
    for _ in range(n):
        # Aplicar la fórmula del método congruencial lineal
        nuevo_valor = (a * pseudoaleatorios[-1] + c) % m
        # Añadir el nuevo valor a la lista
        pseudoaleatorios.append(nuevo_valor)
    
    # Retornar la lista completa de números pseudoaleatorios
    return pseudoaleatorios

# Definición de casos de prueba con diferentes valores para m, a, c, s y n
casos_prueba = [
    # Caso 1: Valores válidos
    {'m': 16, 'a': 5, 'c': 3, 's': 7, 'n': 10},  

    # Caso 2: Diferentes valores válidos
    {'m': 31, 'a': 8, 'c': 3, 's': 5, 'n': 15},  

    # Caso 3: Incremento c=0
    {'m': 12, 'a': 7, 'c': 0, 's': 1, 'n': 5},   
]

# Ejecución de las pruebas con los casos definidos
for i, caso in enumerate(casos_prueba, start=1):
    try:
        # Genera la secuencia pseudoaleatoria para cada caso de prueba
        secuencia = generar_pseudoaleatorios(**caso)
        print(f"Prueba {i}: Entrada {caso} -> Secuencia generada: {secuencia}")
    except Exception as e:
        # Captura y muestra cualquier error que ocurra durante la generación
        print(f"Prueba {i}: Error con entrada {caso} -> {str(e)}")

# Definición de casos de prueba que deberían causar errores debido a entradas inválidas
casos_error = [
    # Error: a < 2
    {'m': 16, 'a': 1, 'c': 3, 's': 7, 'n': 10},  

    # Error: c >= m
    {'m': 16, 'a': 5, 'c': 20, 's': 7, 'n': 10}, 
    
    # Error: s >= m
    {'m': 16, 'a': 5, 'c': 3, 's': 16, 'n': 10}, 

    # Error: n <= 0
    {'m': 16, 'a': 5, 'c': 3, 's': 7, 'n': -5},  
]

# Ejecución de las pruebas que deberían fallar con los casos definidos
for i, caso in enumerate(casos_error, start=1):
    try:
        # Intenta generar la secuencia pseudoaleatoria, lo que debería fallar
        secuencia = generar_pseudoaleatorios(**caso)
        print(f"Prueba con error {i}: Entrada {caso} -> Secuencia generada: {secuencia}")
    except Exception as e:
        # Captura y muestra el error esperado para cada caso inválido
        print(f"Prueba con error {i}: Error con entrada {caso} -> {str(e)}")
