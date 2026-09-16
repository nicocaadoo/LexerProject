import datetime
import threading
import time
import os


# Evidencia 1. Resaltador de sintaxis
# Regina Fernanda Portela Palacios / Nicolás Casillas Larrañaga

# Tabla de acuerdo al DFA
tabla = [
            [0, 8, 9, 9, 10, 11, 11, 12, 1, 1, 2, 6, 19, 0, 11, 19],
            [1, 1, 1, 1, 1, 1, 1, 1, 13, 13, 1, 1, 1, 1, 1, 19],
            [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 2, 6, 3, 13, 13, 19],
            [19, 4, 4, 19, 19, 19, 19, 19, 19, 19, 5, 19, 19, 19, 19, 19],
            [19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 5, 19, 19, 19, 19, 19],
            [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 5, 13, 13, 13, 13, 19],
            [19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 7, 19, 19, 19, 19, 19],
            [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 7, 13, 3, 13, 13, 19],
            [9, 19, 9, 9, 14, 14, 14, 14, 14, 14, 2, 14, 14, 14, 14, 19],
            [14, 9, 9, 9, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 19],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 15, 10, 19],
            [16, 16, 16, 16, 16, 11, 11, 16, 16, 16, 11, 16, 16, 16, 17, 19],
            [18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 19]
        ]

# Cosas que acepta
keywords = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
            'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
            'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

l = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
d = "0123456789"
b = " \t$"
sl = "\n"
e = "eE"

# Función que recibe un archivo .py y regresa un .html coloreado según su tipo
def lexerCategorias(archivo, archivo_salida):
    try: 
        salida = open(archivo_salida, "wt")
        salida.write("<html><body><pre>\n")

        def escribir(color, texto):
            salida.write(f'<span style="color:{color}">{texto}</span>')
        
        with open(archivo) as f:
            for linea in f:
                s = linea + " "
                
                operadores = "+-*/%=<>!&|^"
                delimitatores = ":()[]{},;"
                estado = 0
                p = 0
                lexema = ''
                token = ''
                
                while p < len(s) and estado != 19:
                    c = s[p]
                    
                    # Clasificación
                    if lexema in keywords:
                        col = 14
                    elif c in b:
                        if c == " " and col == 0:
                            escribir("red", " ")
                        col = 0
                    elif c == '-':
                        col = 1
                    elif c == '+':
                        col = 2
                    elif c in operadores:
                        col = 3
                    elif c == '#':
                        col = 4
                    elif c in e and (estado == 2 or estado == 8 or estado == 7):
                        col = 12
                    elif c in l:
                        col = 5
                    elif c == '_':
                        col = 6
                    elif c in delimitatores:
                        col = 7
                    elif c == '"':
                        if estado == 1:
                            lexema += c
                        col = 8
                    elif c == "'":
                        if estado == 1:
                            lexema += c
                        col = 9
                    elif c in d:
                        col = 10
                    elif c == '.':
                        col = 11
                    elif c in sl:
                        col = 13
                    else:
                        col = 15
                
                    # Transición de estados
                    estado = tabla[estado][col]
        
                    # Estados de aceptación
                    if estado == 13:
                        escribir("blue", lexema)
                        lexema = ''
                        p-=1
                        estado = 0
                    elif estado == 14:
                        escribir("fuchsia", lexema)
                        lexema = ''
                        p-=1
                        estado = 0
                    elif estado == 15:
                        escribir("orange", lexema)
                        lexema = ''
                        estado = 0
                        p-=1
                    elif estado == 16:
                        escribir("black", lexema)
                        lexema = ''
                        estado = 0
                        p-=1
                    elif estado == 17:
                        escribir("red", lexema)
                        escribir("red", " ")
                        lexema = ''
                        estado = 0
                        p-=1
                    elif estado == 18:
                        escribir("green", lexema)
                        lexema = ''
                        estado = 0
                        p-=1   
                    elif estado == 19:
                        escribir("purple", "Error")
                    p+=1
                    if estado != 0:
                        lexema += c
                        
                salida.write("\n")

        salida.write("</pre></body></html>")
        salida.close()
    except Exception as error:
        print("No se pudo procesar la ruta: "+ str(archivo))
        print("Error:", error)


## Puedes poner carpetas y archivos mezclados
rutas = [
    "../ThreadLexer/ejemplos",
    "../ThreadLexer/ejemplos/ejemplo5.py",
    "../ThreadLexer/ejemplo6.py"
]

entradas = []
salidas = []

for ruta in rutas:

    # Si es un archivo .py
    if os.path.isfile(ruta):
        if ruta.endswith(".py"):
            entradas.append(ruta)
            salidas.append(ruta.replace(".py", ".html"))

    # Si es una carpeta
    elif os.path.isdir(ruta):
        for elemento in os.listdir(ruta):
            archivo = os.path.join(ruta, elemento)

            if os.path.isfile(archivo) and archivo.endswith(".py"):
                entradas.append(archivo)
                salidas.append(archivo.replace(".py", ".html"))

##Inicias tiempo para procesar secuencialmente
inicio_sec = datetime.datetime.now()

##print(os.path.exists(entradas[0]))
for i in range(len(entradas)):
    lexerCategorias(entradas[i], salidas[i])

##Terminas tiempo para procesar secuencialmente
fin_sec = datetime.datetime.now()
tiempo_secuencial = (fin_sec - inicio_sec).total_seconds()
print("Tiempo Total: " + str(tiempo_secuencial) + "segundos\n")

##Inicias tiempo para procesar en paralelo
inicio_par = datetime.datetime.now()

lista_hilos = []
for i in range(len(entradas)):
    hilo = threading.Thread(target=lexerCategorias, args=(entradas[i], salidas[i]))
    lista_hilos.append(hilo)
    hilo.start()

for hilo in lista_hilos:
    hilo.join()

##Terminas tiempo para procesar en paralelo
fin_par = datetime.datetime.now()
tiempo_paralelo = (fin_par - inicio_par).total_seconds()
print("Tiempo total en paralelo: "+ str(tiempo_paralelo) + " segundos\n")

if tiempo_paralelo > 0:
    speedup = tiempo_secuencial / tiempo_paralelo
    print("Cantidad de archivos procesados: " + str(len(entradas)))
    print("Cantidad de archivos HTML generados: " + str(len(salidas)))
    print("Speedup: "+ str(speedup)+"x")

