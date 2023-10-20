# Analizador de Texto

Este es un programa simple para analizar archivos de texto. Puede calcular estadísticas como el número de palabras, líneas, caracteres, párrafos, promedio de palabras por línea, contar palabras específicas y mostrar las palabras más comunes. También puede extraer frases importantes del texto.

## Requisitos

Este programa utiliza las siguientes bibliotecas de Python:

- `os`
- `re`
- `docx2txt`
- `PyPDF2`
- `collections`
- `nltk`

Asegúrate de tener estas bibliotecas instaladas antes de ejecutar el programa.

## Instalación de NLTK (Natural Language Toolkit)

El programa utiliza NLTK para procesar el texto. Para descargar los recursos necesarios de NLTK, ejecuta los siguientes comandos una vez:

```python
import nltk
nltk.download("punkt")
nltk.download("stopwords")
```

## Uso del Programa

Para utilizar el programa, sigue estos pasos:

1. Ejecuta el programa proporcionando los nombres de los archivos que deseas analizar. Puedes cambiar los nombres de archivo en el ejemplo de uso al final del script:

   ```python
   comparar_archivos("ruta_del_archivo1", "ruta_del_archivo2")
   ```

   Por ejemplo:

   ```python
   comparar_archivos("Analizador de texto/prueba.txt", "Analizador de texto/prueba.pdf")
   ```

2. El programa te pedirá que ingreses una palabra específica que deseas contar en el texto. Proporciona la palabra y presiona Enter.

3. El programa generará estadísticas y mostrará la palabra específica contada, las palabras más comunes y frases importantes.

4. Opcionalmente, el programa te preguntará si deseas guardar los resultados en un archivo. Puedes responder "Sí" o "No". Si eliges guardarlos, se te pedirá que ingreses el nombre del archivo de destino.

5. ¡Listo! Los resultados se mostrarán en la consola y, si lo deseas, también se guardarán en un archivo.


¡Gracias por utilizar el Analizador de Archivos!
