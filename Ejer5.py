"""----------------
-----------------------------------------------------------
ÁNGEL DE JESÚS MÉRIDA JIMÉNEZ - 23661
UNIVERSIDAD DEL VALLE DE GUATEMALA
FACULTAD DE MATEMÁTICA
DEPARTAMENTO DE CIENCIA DE LA COMPUTACIÓN
MATEMÁTICA DISCRETA 1


Actividad: Tarea 3 ejercicio 5
-------------------------------------------------------------
-----------------/"""

def validar_entradas(celdas_memoria, datos):
    # Verifica que la cantidad de celdas de memoria sea un entero positivo
    if not isinstance(celdas_memoria, int) or celdas_memoria <= 0:
        raise ValueError("La cantidad de celdas de memoria debe ser un entero positivo.")
    
    # Verifica que todos los datos sean enteros no negativos
    if not all(isinstance(dato, int) and dato >= 0 for dato in datos):
        raise ValueError("Todos los datos deben ser enteros no negativos.")

def almacenar_datos(celdas_memoria, datos):
    # Validar las entradas antes de continuar
    validar_entradas(celdas_memoria, datos)
    
    # Crear un array para representar la memoria, inicialmente con valores None
    memoria = [None] * celdas_memoria
    
    for dato in datos:
        # Calcular la posición inicial usando la función de dispersión H(n) = n mod m
        posicion = dato % celdas_memoria
        
        # Manejo de colisiones: buscar la siguiente posición disponible
        while memoria[posicion] is not None:
            # Si la posición está ocupada, se busca la siguiente
            posicion = (posicion + 1) % celdas_memoria
        
        # Almacenar el dato en la posición encontrada
        memoria[posicion] = dato
    
    return memoria

# Pruebas del algoritmo con diferentes casos
casos_prueba = [
    # Caso 1: Valores válidos:
    {'celdas_memoria': 11, 'datos': [15, 558, 32, 132, 102, 5, 257]}, 

    # Caso 2: Menos celdas de memoria:
    {'celdas_memoria': 7, 'datos': [10, 20, 30, 40, 50, 60, 70]},    

    # Caso 3: Todos los datos en misma posición inicial  
    {'celdas_memoria': 5, 'datos': [1, 6, 11, 16, 21, 26]},           
]

# Ejecución de las pruebas
for i, caso in enumerate(casos_prueba, start=1):
    try:
        resultado_memoria = almacenar_datos(**caso)
        print(f"Prueba {i}: Entrada {caso} -> Resultado de la memoria: {resultado_memoria}")
    except Exception as e:
        print(f"Prueba {i}: Error con entrada {caso} -> {str(e)}")

# Casos de prueba que deberían lanzar errores
casos_error = [
    # Error: celdas_memoria negativa
    {'celdas_memoria': -11, 'datos': [15, 558, 32]},       

    # Error: dato no entero    
    {'celdas_memoria': 11, 'datos': [15, 558, '32', 132]},     
    
    # Error: dato negativo
    {'celdas_memoria': 11, 'datos': [15, 558, -32, 132]},     

    # Error: celdas_memoria cero
    {'celdas_memoria': 0, 'datos': [15, 558, 32]},             
]

# Ejecución de las pruebas que deberían fallar
for i, caso in enumerate(casos_error, start=1):
    try:
        resultado_memoria = almacenar_datos(**caso)
        print(f"Prueba con error {i}: Entrada {caso} -> Resultado de la memoria: {resultado_memoria}")
    except Exception as e:
        print(f"Prueba con error {i}: Error con entrada {caso} -> {str(e)}")
