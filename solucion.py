# En este archivo debes implementar la función

def reloj_arena(m: int, s: str) -> str:
    if m <= 0:
        return print("Error: La altura debe ser un entero positivo")
    elif s == "":
        return print("Error: El caracter no puede ser vacío")
    
    for i in range(-m+1, m):
        h = abs(i)*2 + 1
        e = m - h//2 - 1
        print((" "*e) + (s*h))