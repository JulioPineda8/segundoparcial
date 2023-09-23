def mostrar_mensaje(mensaje):
    print("*******************************")
    print(mensaje)
    print("*******************************")

def cargar_suma():
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    suma = numero1 + numero2
    print("La suma de los dos números es:", suma)

# Programa principal

mostrar_mensaje("El programa calcula la suma de dos variables ingresadas por teclado.")
cargar_suma()