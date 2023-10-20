import os
import re
import docx2txt
from PyPDF2 import PdfReader
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk

# Descarga los recursos de NLTK (solo necesario una vez)
nltk.download("punkt")
nltk.download("stopwords")

def guardar_resultados(nombre_archivo, contenido):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)

def analizar_archivo(filename):
    # Comprobamos si el archivo existe
    if not os.path.exists(filename):
        print("El archivo no existe")
        return

    # Inicializamos las variables
    content = ""
    file_extension = os.path.splitext(filename)[-1].lower()
    num_words = 0
    num_lines = 0
    num_chars = 0
    num_paragraphs = 0
    avg_words_per_line = 0

    # Leemos el contenido del archivo según su tipo
    if file_extension == ".txt":
        with open(filename, "r") as f:
            content = f.read()
    elif file_extension == ".docx":
        content = docx2txt.process(filename)
    elif file_extension == ".pdf":
        pdf_reader = PdfReader(filename)
        for page in pdf_reader.pages:
            content += page.extract_text()

    # Contamos el número de palabras
    num_words = len(re.findall(r'\b\w+\b', content))

    # Contamos el número de líneas
    num_lines = content.count("\n") + 1

    # Contamos el número de caracteres
    num_chars = len(content)

    # Calculamos el número de párrafos (asumiendo que los párrafos están separados por líneas en blanco)
    paragraphs = re.split(r'\n\s*\n', content)
    num_paragraphs = len(paragraphs)

    # Calculamos el promedio de palabras por línea
    if num_lines > 0:
        avg_words_per_line = num_words / num_lines
    else:
        avg_words_per_line = 0

    # Contar las palabras más comunes
    words = word_tokenize(content)
    filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stopwords.words("english")]
    word_freq = Counter(filtered_words)

    # Imprimir las estadísticas avanzadas
    resultado = f"El archivo '{filename}' tiene:\n"
    resultado += f"- {num_words} palabras\n"
    resultado += f"- {num_lines} líneas\n"
    resultado += f"- {num_chars} caracteres\n"
    resultado += f"- {num_paragraphs} párrafos\n"
    resultado += f"- Promedio de palabras por línea: {avg_words_per_line:.2f}\n"

    # Solicitar al usuario la palabra específica que desea contar
    word_to_count = input("Ingrese la palabra específica que desea contar: ")

    # Contar el número de veces que aparece la palabra específica en el contenido
    word_count = content.lower().count(word_to_count.lower())
    resultado += f"La palabra '{word_to_count}' aparece {word_count} veces en el archivo '{filename}'.\n"

    # Imprimir las palabras más comunes
    most_common_words = word_freq.most_common(10)
    resultado += "Las palabras más comunes son:\n"
    for word, freq in most_common_words:
        resultado += f"{word}: {freq} veces\n"

    # Extraer frases importantes (puedes ajustar el número de frases)
    important_sentences = sent_tokenize(content)[:5]
    resultado += "Frases importantes:\n"
    for i, sentence in enumerate(important_sentences, 1):
        resultado += f"{i}. {sentence}\n"

    # Imprimir los resultados en la consola
    print(resultado)

    # Dar opción de guardar los resultados en un archivo
    guardar = input("¿Desea guardar los resultados en un archivo? (Sí/No): ").strip().lower()
    if guardar == "si" or guardar == "sí":
        nombre_archivo = input("Ingrese el nombre del archivo de destino: ")
        guardar_resultados(nombre_archivo, resultado)
        print(f"Resultados guardados en '{nombre_archivo}'")

def comparar_archivos(archivo1, archivo2):
    print(f"Comparación entre '{archivo1}' y '{archivo2}':")
    print("Archivo 1:")
    resultado_archivo1 = analizar_archivo(archivo1)
    print("\nArchivo 2:")
    resultado_archivo2 = analizar_archivo(archivo2)

# Ejemplo de uso:
comparar_archivos("Analizador de texto\prueba.txt", "Analizador de texto\prueba.pdf")
