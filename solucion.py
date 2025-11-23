# En este archivo debes implementar la función

def reloj_arena(m: int, s: str) -> str:
    if m <= 0:
        return print("Error: La altura debe ser un entero positivo")
    
    for i in range(-m+1, m):
        # Altura
        h = abs(i)*2 + 1
        # Espacio a centrar
        e = m - h//2 - 1
        
        print((" "*e) + (s*h))