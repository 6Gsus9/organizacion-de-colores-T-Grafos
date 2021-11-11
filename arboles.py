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
    
def generar_siguiente(actual, visitados):
    i = nombres.index(actual.nombre)
    
    for k in range(len(mapa[i])):
        #m = mapa[i].index(k)
        
        siguiente = Nodo(padre = actual, nombre = nombres[k])
        
        
        if mapa[i][k] == 1 and siguiente not in visitados:
            
            return siguiente
    return None

nombres = ["rojo", "malva","verde","ambar","cian","burdeos",'amarillo','naranja']

mapa = [[0, 0, 1, 1, 0, 1, 1, 1], [0, 0, 0, 0, 1, 0, 1, 1], [1, 0, 0, 0, 0, 1, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 0, 1, 0], [1, 1, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 0, 1, 0]]


actual = Nodo(nombre = "rojo")

pila = [actual]
visitados = []
while  len(pila) != len(nombres):
    
    a = generar_siguiente(actual,pila)
    if a is not None and a not in pila:
        visitados.append(actual)
        actual = a
        pila.append(actual)
    else:
        if len(pila) == 1:
            pila.pop()
            print("No existe solución al problema")
            break
        else:
            pila.pop()
            actual = pila[-1]
        
print("El camino a seguir es %s"%(pila))