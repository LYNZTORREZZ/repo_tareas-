class Nodo:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, codigo, descripcion):
        nuevo = Nodo(codigo, descripcion)

        # Agregar al final de la lista
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.cabeza

        while actual is not None:
            print(actual.codigo, actual.descripcion)
            actual = actual.siguiente


class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if len(self.items) == 0:
            print("La pila esta vacia")
            return None

        return self.items.pop()


class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if len(self.items) == 0:
            print("La cola esta vacia")
            return None

        return self.items.pop(0)


# Pruebas del archivo institucional

lista = ListaEnlazada()

lista.agregar("AR01", "Acta")
lista.agregar("AR02", "Memorandum")
lista.agregar("AR03", "Informe")

print("ARCHIVO INSTITUCIONAL")
print("\nDocumentos guardados:")
lista.mostrar()

# Mostrar la lista sin cambiar los enlaces
print("\nMostrar la lista otra vez:")
lista.mostrar()

# Prueba de la pila
pila = Pila()

pila.apilar("AR01")
pila.apilar("AR02")
pila.apilar("AR03")

print("\nPrueba de la pila:")
print(pila.desapilar())
print(pila.desapilar())
print(pila.desapilar())

# Prueba de la cola
cola = Cola()

cola.encolar("AR01")
cola.encolar("AR02")
cola.encolar("AR03")

print("\nPrueba de la cola:")
print(cola.desencolar())
print(cola.desencolar())
print(cola.desencolar())