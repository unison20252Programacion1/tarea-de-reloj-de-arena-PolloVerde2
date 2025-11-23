# En este archivo debes implementar la función

def reloj_arena(m: int, s: str) -> str:
    if m <= 0:
        return print("Error: La altura debe ser un entero positivo")
    
    for i in range(-m, m, 2):
        # Cantidad de caracteres a imprimir
        h = abs(i + 1) + 1
        # Cantidad de espacios para centrar
        e = (m - h) // 2
        # Imprimir figura
        print((" " * e) + (s * h))