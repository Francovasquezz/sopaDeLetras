import random

#FUNCIONES
def seleccionarTamanio():
    print("¿Con que tablero desea iniciar la partida?")
    print()
        #El usuario debe elegir la dificultad del juego
    print("Elija con que dificultad va a jugar la sopa de letras:")
    while True:
        try:
            print()
            tamanio=input("Ingrese F para jugar con el tablero facil, M para jugar con el tablero medio o D para jugar con el tablero dificil: ")
            tamanio=tamanio.upper()
            assert tamanio=="F" or tamanio=="M" or tamanio=="D"
            break
        except AssertionError:
            print("Solo puede ingresar F, M o D. Intente nuevamente.")
        #Asignamos la cantidad de celdas segun el tamanio elegido

    if tamanio=="F":
        n=10 # Si es facil el tablero es de 10x10
    elif tamanio=="M":
        n=15 # Si es medio el tablero es de 15x15
    else:
        n=20 # Si es dificil el tablero es de 20x20
    return n

def dificultadJuego(n):
    if n==10: 
        d=8 #Si la dificultad es facil, se deberan descubrir 8 palabras
    elif n==15: 
        d=12 #Si la dificultad es media, se deberan descubrir 12 palabras
    else:
        d=16 #Si la dificultad es dificil, se deberan descubrir 16 palabras
    return d

def abrirArchivo(d, palabrasDelJuego):
    
    """La función abrirArchivo recibe dos parámetros: d que representa la cantidad de palabras a seleccionar
       y palabrasDelJuego que es un conjunto donde se almacenarán las palabras seleccionadas.
       Se utiliza un bloque try-except-finally para manejar las posibles excepciones que puedan ocurrir
       al abrir y leer el archivo."""
    try:
        archivo=open(r"palabras.txt","rt")#se abre el archivo ubicado en la ruta especificada
        limite=250
        lineasRandom=[]
        """Se genera una lista lineasRandom con números aleatorios entre 0 y 250. Estos números representarán
            las líneas del archivo que se leerán de manera aleatoria."""
        for i in range(d+10):
            linea=random.randint(0,limite) 
            lineasRandom.append(linea) 
        lineasRandom.sort()
        inicio=0
        pos=0
        while len(palabrasDelJuego)<d: # se lee el archivo línea por línea
            for i in range(inicio,lineasRandom[pos]): 
                archivo.readline() #Leemos las lineas pero no las guardamos
            palabra=archivo.readline()
            palabra=palabra.rstrip("\n")
            if len(palabra)<n: # Se guardan las palabras que cumplan con esta condicion a la variable de abajo
                palabrasDelJuego.add(palabra)
            inicio=lineasRandom[pos]
            pos=pos+1
    except FileNotFoundError:
        print("Hubo un error al seleccionar las palabras de la sopa de letras")
    except OSError:
        print("Ocurrio un problema")
    finally:
        archivo.close() #Al final del bloque try, se cierra el archivo 
    print()
    print("Las palabras que se deben buscar son: "+ ', '.join(palabrasDelJuego)) #Se muestran las palabras que se deben buscar
    print()
    return palabrasDelJuego
    
def llenarMatriz(matriz, extension): # Función para rellenar la matriz con palabras
    n = len(matriz)  # Obtener el tamaño de la matriz
    palabrasParaUbicar = list(palabrasDelJuego)  # Crear una copia de las palabras a ubicar
    while len(palabrasParaUbicar) > 0:  # Hasta insertar todas las palabras de la lista
        palabra = palabrasParaUbicar[0]  # Seleccionar la próxima palabra de la lista
        orientacion = random.randint(1, extension)  # Elegir una orientación aleatoria para la palabra
        filaInicio = random.randint(0, n - 1)  # Elegir una fila aleatoria para comenzar la palabra
        columnaInicio = random.randint(0, n - 1)  # Elegir una columna aleatoria para comenzar la palabra
        ubicada = PosicionP(orientacion, columnaInicio, palabra, filaInicio, palabrasParaUbicar)
        # Verificar si la palabra se puede ubicar en la posición elegida y actualizar la lista de palabras restantes

    for f in range(n):  # Recorrer las filas de la matriz
        for c in range(n):  # Recorrer las columnas de la matriz
            posicion = random.randint(0, 26)  # Generar una posición aleatoria para seleccionar una letra del abecedario
            if matriz[f][c] == 0:  # Si la celda está vacía
                matriz[f][c] = abecedario[posicion]  # Rellenar la celda con una letra aleatoria del abecedario
  

#comienzo de funciones de orientacion
def verticalabajo(filaInicio, palabra,columnaInicio):
    """Agrega una palabra en vertical hacia abajo en la matriz si
    hay espacio disponible y no hay letras en las celdas correspondientes.
    Devuelve True si la palabra se agrego bien"""
    if n-filaInicio>=len(palabra):#si la palabra entra en las celdas
        concatenar=""
        ceros=""
        for i in range(len(palabra)):
             ceros=ceros+"0"#largo de la palabra en ceros
        for i in range(len(palabra)):
            concatenar=concatenar+str(matriz[filaInicio+i][columnaInicio]) #letras contenidas de la matriz
        if concatenar==ceros: #se agrega la palabra si esta vacio ese espacio
            for i in range(len(palabra)): 
                 matriz[filaInicio+i][columnaInicio]=palabra[i]
            return True

def verticalarriba(filaInicio, palabra,columnaInicio):
    """Agrega una palabra en vertical hacia arriba en la matriz si
    hay espacio disponible y no hay letras en las celdas correspondientes.
    Devuelve True si la palabra se agrego bien"""
    if filaInicio>=len(palabra):#si la palabra entra en las celdas
        concatenar=""
        ceros=""
        for i in range(len(palabra)):
            ceros=ceros+"0"
        for i in range(len(palabra)):
            concatenar=concatenar+str(matriz[filaInicio-i][columnaInicio])
        if concatenar==ceros:#se agrega la palabra si esta vacio ese espacio
            for i in range(len(palabra)):
                matriz[filaInicio-i][columnaInicio]=palabra[i]
            return True

def horizontaladerecha(columnaInicio, palabra, filaInicio):
    """Agrega una palabra en horizontal hacia la derecha en la matriz si
    hay espacio disponible y no hay letras en las celdas correspondientes.
    Devuelve True si la palabra se agrego bien"""
    if n-columnaInicio>=len(palabra):#si la palabra entra en las celdas
        concatenar=""
        ceros=""
        for i in range(len(palabra)):
             ceros=ceros+"0"
        for i in range(len(palabra)):
            concatenar=concatenar+str(matriz[filaInicio][columnaInicio+i])
        if concatenar==ceros:#se agrega la palabra si esta vacio ese espacio
            for i in range(len(palabra)):
                matriz[filaInicio][columnaInicio+i]=palabra[i]
            return True
            
def horizontalaizquierda(columnaInicio, palabra, filaInicio):
    """Agrega una palabra en horizontal pero hacia la izquierda en la matriz si
    hay espacio disponible y no hay letras en las celdas correspondientes.
    Devuelve True si la palabra se agrego bien"""
    if columnaInicio>=len(palabra):#si la palabra entra en las celdas
        concatenar=""
        ceros=""
        for i in range(len(palabra)):
            ceros=ceros+"0"
        for i in range(len(palabra)):
            concatenar=concatenar+str(matriz[filaInicio][columnaInicio-i])
        if concatenar==ceros:#se agrega la palabra si esta vacio ese espacio
            for i in range(len(palabra)):
                matriz[filaInicio][columnaInicio-i]=palabra[i]
            return True
            
def diagonalarribaderecha(columnaInicio, palabra, filaInicio):
    """Agrega una palabra en diagonal hacia arriba de izquierda a derecha en la matriz si
    hay espacio disponible y no hay letras en las celdas correspondientes.
    Devuelve True si la palabra se agrego bien"""
    if n-columnaInicio>=len(palabra) and filaInicio>=len(palabra):#si la palabra entra en las celdas
        concatenar=""
        ceros=""
        for i in range(len(palabra)):
            ceros=ceros+"0"
        for i in range(len(palabra)):
            concatenar=concatenar+str(matriz[filaInicio-i][columnaInicio+i])
        if concatenar==ceros:#se agrega la palabra si esta vacio ese espacio
            for i in range(len(palabra)):
                matriz[filaInicio-i][columnaInicio+i]=palabra[i]
            return True
            
def diagonalabajoderecha(columnaInicio, palabra, filaInicio):
    """Agrega una palabra en diagonal hacia abajo de izquierda a derecha en la matriz si
    hay espacio disponible y no hay letras en las celdas correspondientes.
    Devuelve True si la palabra se agrego bien"""
    if n-columnaInicio>=len(palabra) and n-filaInicio>=len(palabra):#si la palabra entra en las celdas
        concatenar=""
        ceros=""
        for i in range(len(palabra)):
            ceros=ceros+"0"
        for i in range(len(palabra)):
            concatenar=concatenar+str(matriz[filaInicio+i][columnaInicio+i])
        if concatenar==ceros:#se agrega la palabra si esta vacio ese espacio
            for i in range(len(palabra)):
                matriz[filaInicio+i][columnaInicio+i]=palabra[i]
            return True
            
def diagonalarribaizquierda(columnaInicio, palabra, filaInicio):
    """Agrega una palabra en diagonal hacia arriba de derecha a izquierda en la matriz si
    hay espacio disponible y no hay letras en las celdas correspondientes.
    Devuelve True si la palabra se agrego bien"""
    if columnaInicio>=len(palabra) and filaInicio>=len(palabra):#si la palabra entra en las celdas
        concatenar=""
        ceros=""
        for i in range(len(palabra)):
            ceros=ceros+"0"
        for i in range(len(palabra)):
            concatenar=concatenar+str(matriz[filaInicio-i][columnaInicio-i])
        if concatenar==ceros:#se agrega la palabra si esta vacio ese espacio
            for i in range(len(palabra)):
                matriz[filaInicio-i][columnaInicio-i]=palabra[i]
            return True
            
def diagonalabajoizquierda(columnaInicio, palabra, filaInicio):       
    """Agrega una palabra en diagonal hacia abajo de derecha a izquierda en la matriz si
    hay espacio disponible y no hay letras en las celdas correspondientes.
    Devuelve True si la palabra se agrego bien"""
    if n-columnaInicio>=len(palabra) and n-filaInicio>=len(palabra):#si la palabra entra en las celdas
        concatenar=""
        ceros=""
        for i in range(len(palabra)):
            ceros=ceros+"0"
        for i in range(len(palabra)):
            concatenar=concatenar+str(matriz[filaInicio+i][columnaInicio+i])
        if concatenar==ceros:#se agrega la palabra si esta vacio ese espacio
            for i in range(len(palabra)):
                matriz[filaInicio+i][columnaInicio+i]=palabra[i]
            return True

#fin de funciones de orientacion


def PosicionP(orientacion,columnaInicio, palabra, filaInicio,palabrasParaUbicar):
    '''Usamos las funciones de orientacion para ubicar las palabras en la matriz'''
    if orientacion==1: #Vertical
        ubicada=verticalabajo(filaInicio, palabra, columnaInicio)
        if ubicada==True:
            palabrasParaUbicar.pop(0) #Borramos la palabra de la lista porque ya fue ubicada
    elif orientacion==2: #Horizontal
        ubicada=horizontaladerecha(columnaInicio, palabra, filaInicio)
        if ubicada==True:
            palabrasParaUbicar.pop(0)
    elif orientacion==3: #Diagonal de izq a derecha y hacia abajo
        ubicada=diagonalabajoderecha(columnaInicio, palabra, filaInicio)
        if ubicada==True:
            palabrasParaUbicar.pop(0)
    elif orientacion==4: #Vertical invertida
        ubicada=verticalarriba(filaInicio, palabra, columnaInicio)
        if ubicada==True:
            palabrasParaUbicar.pop(0)
    elif orientacion==5: #Horizontal invertida
        ubicada=horizontalaizquierda(columnaInicio, palabra, filaInicio)
        if ubicada==True:
            palabrasParaUbicar.pop(0)
    elif orientacion==6: #Diagonal de izquierda a derecha y hacia arriba
        ubicada=diagonalarribaderecha(columnaInicio, palabra, filaInicio)
        if ubicada==True:
            palabrasParaUbicar.pop(0)
    elif orientacion==7: #Diagonal de derecha a izquierda y hacia arriba
        ubicada=diagonalarribaizquierda(columnaInicio, palabra, filaInicio)
        if ubicada==True:
            palabrasParaUbicar.pop(0)
    elif orientacion==8: #Diagonal de derecha a izquierda y hacia abajo
        ubicada=diagonalabajoizquierda(columnaInicio, palabra, filaInicio)
        if ubicada==True:
            palabrasParaUbicar.pop(0)

def imprimirMatriz(matriz):
    print ("    ","%2s"%"1",end="") #Enumeramos las columnas
    for i in range(len(matriz)-1):
        print("%4s"%str(i+2),end="")
    print()
    print ("    ","%2s"%"-", end="")
    for i in range(len(matriz)-1):
        print("%4s"%"-",end="")
    print()
    x=0
    for i in range(len(matriz)):
        print (abecedario[x], "|",end = "")
        imprimirLista(matriz[i])
        print()
        x=x+1
        
def imprimirLista(lista, inicio=0):
    if inicio<len(lista):
        print("%4s" %lista[inicio],end="")
        imprimirLista(lista, inicio+1)
        
def imprimir(matriz, filaInicio, columnaInicio, filaFin, columnaFin, palabra, coordenadas):
    filas=len(matriz)
    columnas=len(matriz[0])
    coordNuevas= unirCoordenadas(matriz,filaInicio,columnaInicio,filaFin,columnaFin)
    coordenadas=coordenadas+coordNuevas   
    print ("    ","%2s"%"1",end="") #Enumeramos las columnas
    for i in range(len(matriz)-1):
        print("%4s"%str(i+2),end="")
    print()
    print ("    ","%2s"%"-", end="")
    for i in range(len(matriz)-1):
        print("%4s"%"-",end="")
    print()  
    x = 0
    for f in range (filas):                #Enumeramos las filas con letras
        print (abecedario[x], "|",end = "") 
        x = x + 1
        for c in range(columnas):
            print("%4s" %matriz[f][c], end="")
        print()
    return coordenadas

def celda_correcta():
    while True:
        try:
            celda=input()
            letra=celda[0].upper()
            assert letra.isalpha(), "Primero de debe ir la letra de la fila seleccionada. Ingrese la celda otra vez:"
            if n==10:
                assert letra in abecedario[:10], "La fila ingresada esta fuera de rango. Ingrese la celda otra vez:"
                if len(celda)==2:
                    nro=int(celda[1])
                    assert nro<=10,"La columna ingresada esta fuera de rango. Ingrese la celda otra vez:"
                else:
                    nro=int(celda[1]+celda[2])
                    assert nro<=10,"La columna ingresada esta fuera de rango. Ingrese la celda otra vez:"
            elif n==15:
                assert letra in abecedario[:15], "La fila ingresada esta fuera de rango. Ingrese la celda otra vez:"
                if len(celda)==2:
                    nro=int(celda[1])
                    assert nro<=15,"La columna ingresada esta fuera de rango. Ingrese la celda otra vez:"
                else:
                    nro=int(celda[1]+celda[2])
                    assert nro<=15,"La columna ingresada esta fuera de rango. Ingrese la celda otra vez:"
            elif n==20:
                assert letra in abecedario[:20], "La fila ingresada esta fuera de rango. Ingrese la celda otra vez:"
                if len(celda)==2:
                    nro=int(celda[1])
                    assert nro<=20,"La columna ingresada esta fuera de rango. Ingrese la celda otra vez:"
                else:
                    nro=int(celda[1]+celda[2])
                    assert nro<=20,"La columna ingresada esta fuera de rango. Ingrese la celda otra vez:"
            assert str(nro).isdigit(), "La segunda parte de la celda debe ser un numero de fila. Ingrese la celda otra vez:"
            break
        except AssertionError as mensaje:
            print(mensaje)
        except ValueError:
            print("Solo caracteres alfanumericos. Ingrese la celda otra vez:")
    strAbecedario=''.join(abecedario)
    fila=strAbecedario.find(letra)
    return fila,nro #tupla

def unirLetras (mat,coorX1,coorY1,coorX2,coorY2): 
    palabra = mat[coorX1][coorY1] #palabra que se forma entre las coordenadas enviadas
    while coorX1 != coorX2 or coorY1 != coorY2:
        if coorX1 < coorX2:
            coorX1 += 1
        elif coorX1 > coorX2:
            coorX1 -= 1
            
        if coorY1 < coorY2:
            coorY1 += 1
        elif coorY1 > coorY2:
            coorY1 -= 1
        palabra = palabra + mat[coorX1][coorY1]
    return palabra

def unirCoordenadas (mat,coorX1,coorY1,coorX2,coorY2):
    coordenadas=[]
    coordenadas.append((coorX1,coorY1-1)) #palabra que se forma entre las coordenadas enviadas
    while coorX1 != coorX2 or coorY1 != coorY2:
        if coorX1 < coorX2:
            coorX1 += 1
        elif coorX1 > coorX2:
            coorX1 -= 1
            
        if coorY1 < coorY2:
            coorY1 += 1
        elif coorY1 > coorY2:
            coorY1 -= 1
        encontradas.append((coorX1,coorY1-1))
    return coordenadas

        
#PROGRAMA PRINCIPAL
print("Sopa de letras:")
print()

terminar = ""

while terminar == "":
    n=seleccionarTamanio()
    d=dificultadJuego(n)
    palabrasDelJuego=set() #Creamos un conjunto en donde vamos a agregar las palabras que seran usadas en el juego
    palabrasDelJuego=abrirArchivo(d, palabrasDelJuego)
    matriz=[[0]*(n) for i in range(n)]
    abecedario = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    llenarMatriz(matriz)
    imprimirMatriz(matriz)
    print()    
    #empieza el juego
    escape="" #posibilidad de salir del juego
    palabrasRestantes=list(palabrasDelJuego)
    while len(palabrasRestantes)>0 and escape=="":
        print()
        print("Ingrese las coordenadas del comienzo de la palabra encontrada de la siguiente forma('A1'): ")
        filaInicio, columnaInicio=celda_correcta()
        print("Ingrese las coordenadas en donde termina la palabra encontrada de la siguiente forma('A1'): ")
        filaFin, columnaFin=celda_correcta()
        #Formamos la palabra que se encuentra entre los casilleros elegidos
        palabraFormada=unirLetras(matriz,filaInicio,columnaInicio-1,filaFin,columnaFin-1)#Le restamos 1 porque el usuario empieza a contar en 1, no en 0
        if palabraFormada in palabrasDelJuego: #Si es una de las palabras que tenia que encontrar, ha cumplido el objetivo
            print("¡Encontraste una palabra! La palabra encontrada fue: ", palabraFormada)
            if palabraFormada in palabrasRestantes:
                palabrasRestantes.remove(palabraFormada)
            if len(palabrasRestantes)>0:
                print("Todavia quedan por encontrar estas palabras:"+', '.join(palabrasRestantes))
                encontradas=[]
                print()
                encontradas+=imprimir(matriz, filaInicio, columnaInicio, filaFin, columnaFin, palabraFormada, encontradas)
                print()
                escape=input("Para SALIR del juego ingrese 1, si desea CONTINUAR presione enter: ")
                print ()
        else:
            print("La palabra seleccionada no esta en el juego, intente nuevamente")
            print ()
            escape=input("Para salir del juego ingrese 1, si desea continuar presione enter: ")
    if escape=="":
        print()
        print("¡FELICIDADES! Completaste el juego.")
    else:
        print()
        print("JUEGO FINALIZADO")
    print ()
    terminar = input ("Para salir del juego ingrese 1, si quiere jugar nuevamente presione enter: ") 
    if terminar == "":
        print ("-"*250)
print("FIN DEL JUEGO")
