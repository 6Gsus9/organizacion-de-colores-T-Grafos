#importacion de librerias 
# random para organizar aleatoriamente la lista de colores
#time para mirar el tiempo de ejecucion por lista 
import random
import time
tI=time.time()
#se genera los datos a usar (en este caso colores)
colores = ["rojo", "malva","verde","ambar","cian","burdeos","naranja","amarillo","rosado","lima","violeta","magenta","fucsia","granate","caoba","marron","oliva","esmeralda","cerceta","añil","vino","lacre","cobre","dorado","chartreuse", "turquesa","zafiro","amatista","purpeo","fandango","coral","salmon","melon","crema","maiz","menta","aguamarina","celeste","bigaro","lavanda","pardo","ante","arena","beigis","blanco","negro","cafe","caqui","canela","chocolate","herrube","leon","ocre","rufo","secuoya","sepia","senia","mengue","rojo sangre"]
colores = random.sample(colores, len(colores)) #### sé organizan de forma aleatoria

# colores= ['cerceta', 'salmon', 'ocre', 'herrube', 'burdeos', 'senia', 'beigis', 'celeste', 'zafiro', 'lima', 'arena', 'mengue', 'fandango', 'chartreuse', 'naranja', 'coral', 'pardo', 'rufo', 'añil', 'ambar', 'amatista', 'blanco', 'oliva', 'sepia', 'melon', 'fucsia', 'vino', 'magenta', 'secuoya', 'rojo sangre', 'granate', 'bigaro', 'lacre', 'amarillo', 'ante', 'rojo', 'violeta', 'aguamarina', 'canela', 'purpeo', 'cafe', 'leon', 'caqui', 'rosado', 'crema', 'chocolate', 'lavanda', 'maiz', 'turquesa', 'dorado', 'negro', 'esmeralda', 'malva', 'cian', 'menta', 'marron', 'caoba', 'verde', 'cobre']
print(colores)
#fuente de colores
#https://www.mundo.com/cultura/lista-de-todos-los-colores-del-mundo/

vertices=["rojo"]
aristas = []

##### Matriz de adyacencia
matriz = [[0 for y in colores ] for x in colores]
matriz1 = [[0 for y in colores ] for x in colores]

#Variable para crear las aristas sin repetir el inverso
contador = 0

#generador de arirstas adyacentes
while len(vertices)!= len(colores):
    
    for i in colores:
        if i == vertices[contador] or i in vertices:
            continue
        else:
            for j in vertices[contador]:
                if j in i and len(vertices[contador]) != len(i):
                    aristas.append((vertices[contador],i))
                    break
            
    contador+=1
    vertices.append(colores[contador])

#creacion de matriz de adyacencia
for i in colores:
    for j in vertices:
        if (i,j) in aristas or (j,i) in aristas:
            matriz[colores.index(i)][vertices.index(j)]=1
            matriz1[colores.index(i)][vertices.index(j)]=1
              
            
#print(matriz)


#Clase para la creacion de objetos tipo nodos
class Nodo:
    padre = None
    nombre = ""
    def __init__(self, padre=None, nombre=""):
        self.padre = padre
        self.nombre = nombre
    def __eq__(self, otro):
        return self.nombre == otro.nombre
    def __str__(self):
        return self.nombre
    def __repr__(self):
        return self.__str__()
    

#Funcion que genera las hojas de los nodos
def generar_siguiente(actual, visitados):
    i = nombres.index(actual.nombre)
    
    for k in range(len(mapa[i])):
        #m = mapa[i].index(k)
        
        siguiente = Nodo(padre = actual, nombre = nombres[k])
        
        
        if mapa[i][k] == 1 and siguiente not in visitados and ((siguiente.padre.nombre,siguiente.nombre)  in aristas or (siguiente.nombre,siguiente.padre.nombre)  in aristas) :
            
            return siguiente
    return None

nombres = colores

mapa = matriz.copy()

#Iniciacion de camino Hamiltoniano
actual = Nodo(nombre = vertices[0])

#Lista que contiene el camino
pila = [actual]


while  len(pila) != len(nombres): #Condicion que el camino tenga la misma cantidad de vertices
    
    a = generar_siguiente(actual,pila) #Hoja generada desde la ultima posicion del camino
    if a is not None and a not in pila:
        actual = a
        pila.append(actual)
    else:
        if len(pila) == 1:
            pila.pop()
            print("No existe solución al problema")
            break
        else:
            m = pila.pop()
            mapa[nombres.index(pila[-1].nombre)][nombres.index(m.nombre)]=0
            actual = pila[-1]
            mapa[nombres.index(m.nombre)]=matriz1[nombres.index(m.nombre)].copy()
        
print("El camino a seguir es %s"%(pila))
tf=time.time()

print(tf-tI)