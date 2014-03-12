class tree:
    def __init__(self, val = None, izq = None, der = None):
        self.valor = val
        self.izquierda = izq
        self.derecha = der

    def __str__(self):
        return "(" + (str(self.izquierda) \
                      if self.izquierda != None \
                      else "()") \
                + "(" + str(self.valor) + ")" \
                    + (str(self.derecha) \
                      if self.derecha != None \
                      else "()") \
                + ")"


def busqueda_por_caracteristica(t, caracteristica):
    return [None] if t == None \
           else [t] if t.valor[1::] == caracteristica \
           else busqueda_por_caracteristica(t.izquierda, caracteristica) + \
           busqueda_por_caracteristica(t.derecha, caracteristica)
        


clue = tree("Clue",
            tree("CHombre",
                 tree("CEs alto",
                      tree("Daza"),
                      tree("CTiene lentes",
                           tree("Sebastian"),
                           tree("Pablo")
                      )
                 )
            ),
            tree("CMujer",
                 tree("CTiene lentes",
                      tree("Laura")
                      )
                 )
            )

leaf = lambda t: t.derecha == None and t.izquierda == None

def i_hojas(t, f = False):
    if t.izquierda == None and t.derecha == None: #Es hoja
            print(t.valor)
    elif t.izquierda != None and not leaf(t.izquierda):
        if t.izquierda != None:
            i_hojas(t.izquierda, True)
        i_hojas(t.derecha, True)
    elif t.valor in ["CHombre", "CMujer"]:
        if t.izquierda != None:
            i_hojas(t.izquierda, True)
        if t.derecha != None:
            i_hojas(t.derecha, True)
    else:
        if t.izquierda != None:
            i_hojas(t.izquierda)

#print(clue)
print("Hombre:")
[i_hojas(t) for t in list(filter(lambda x: type(x) == tree,busqueda_por_caracteristica(clue, "Tiene lentes")))]
