import os

# Nombre del archivo a analizar
filename = "Ruta donde se encuentra el documento"

# Comprobamos si el archivo existe
if not os.path.exists(filename):
    print("El archivo no existe")
    exit()

# Abrimos el archivo en modo lectura
with open(filename, "r") as f:
    # Leemos todo el contenido del archivo
    content = f.read()

    # Contamos el número de palabras
    num_words = len(content.split())

    # Contamos el número de líneas
    num_lines = content.count("\n") + 1

    # Contamos el número de caracteres
    num_chars = len(content)

# Imprimimos las estadísticas
print(f"El archivo '{filename}' tiene:")
print(f"- {num_words} palabras")
print(f"- {num_lines} líneas")
print(f"- {num_chars} caracteres")
