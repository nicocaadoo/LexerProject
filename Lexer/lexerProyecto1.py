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
def lexerCategorias(archivo):
    
    salida = open("resultado.html", "wt")
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

# Prueba
lexerCategorias("../Lexer/ejemplo.py")