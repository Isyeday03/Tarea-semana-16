# Operaciones con archivos de texto en Python
# Este programa demuestra cómo crear, escribir, leer y cerrar archivos de texto

def main():
    # 1. ESCRITURA DE ARCHIVO DE TEXTO
    
    # Abrimos el archivo en modo escritura ('w')
    # Si el archivo no existe, se creará. Si existe, se sobrescribirá
    print("Creando y escribiendo en el archivo 'my_notes.txt'...")
    
    archivo_escritura = open('my_notes.txt', 'w')
    
    # Escribimos tres líneas de notas personales
    archivo_escritura.write("Primera nota: Python es un lenguaje versátil y fácil de aprender.\n")
    archivo_escritura.write("Segunda nota: La manipulación de archivos es una habilidad fundamental en programación.\n")
    archivo_escritura.write("Tercera nota: Recuerda siempre cerrar los archivos después de usarlos.\n")
    
    # Cerramos el archivo después de escribir
    archivo_escritura.close()
    print("Archivo creado y escrito correctamente.")
    
    # 2. LECTURA DE ARCHIVO DE TEXTO
    
    print("\nLeyendo el archivo 'my_notes.txt' línea a línea:")
    
    # Abrimos el archivo en modo lectura ('r')
    archivo_lectura = open('my_notes.txt', 'r')
    
    # Leemos y mostramos el contenido línea por línea
    linea = archivo_lectura.readline()
    contador = 1
    
    # Mientras haya líneas para leer (no sea una cadena vacía)
    while linea:
        print(f"Línea {contador}: {linea}", end="")  # end="" evita doble salto de línea
        linea = archivo_lectura.readline()
        contador += 1
    
    # 3. CIERRE DE ARCHIVOS
    
    # Cerramos el archivo después de leer
    archivo_lectura.close()
    print("\nArchivo cerrado correctamente.")

# Ejecutamos la función principal
if __name__ == "__main__":
    main()