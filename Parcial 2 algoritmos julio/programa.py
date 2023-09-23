import sys
import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_area_rectangulo(largo, ancho):
    return largo * ancho

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def main():
    if len(sys.argv) < 2:
        print("Uso: python calcular_areas.py figura1│figura2│...")
        sys.exit(1)

    figuras = sys.argv[1].split("│")
    areas = []

    for i, figura in enumerate(figuras):
        parametros = figura.split(",")
        tipo = parametros[0].split("=")[0]
        
        if tipo == "circulo":
            radio = float(parametros[0].split("=")[1])
            area = calcular_area_circulo(radio)
        elif tipo == "rectangulo":
            largo = float(parametros[1].split("=")[1])
            ancho = float(parametros[0].split("=")[1])
            area = calcular_area_rectangulo(largo, ancho)
        elif tipo == "triangulo":
            base = float(parametros[0].split("=")[1])
            altura = float(parametros[1].split("=")[1])
            area = calcular_area_triangulo(base, altura)
        else:
            print(f"Figura {i+1}: Tipo de figura no reconocido")
            continue

        areas.append(area)
        print(f"Área {tipo} {i+1} = {area:.2f}")

    if len(areas) > 1:
        total_area = sum(areas)
        print(f"Área total = {total_area:.2f}")

if __name__ == "__main__":
    main()