import time

inicio = time.time()

nombre_archivo = "./numeros_1_a_100000.txt"

# Creando y escribiendo en el archivo
with open(nombre_archivo, 'w') as archivo:
    for numero in range(1, 100001):
        archivo.write(f"{numero}\n")

fin = time.time()
tiempo_ejecucion = fin - inicio
print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")
