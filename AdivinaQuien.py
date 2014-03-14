#JUAN SEBASTIAN OTÁLORA LEGUIZAMON 20121020025
#PABLO ANDRES DORADO SUAREZ 20121020036
#JULIAN ANDRES FORERO RODRIGUEZ 20121020024

class tree():
    def __init__(self , valor  , izquierda=None , derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

def entrada(preg):
    print preg
    return raw_input('Respuesta : \t 1) Si \t 2) No\n')

def busqueda_rec(arbol):
    if arbol.izquierda==None:
        return arbol.valor
    else:
        if entrada(arbol.valor)=='1':
            return busqueda_rec(arbol.izquierda)
        else:
            return busqueda_rec(arbol.derecha)           

arbol = tree("Es hombre",
             tree("Es calvo",
                   tree("Tiene bigote",
                        tree("Con lunar",
                             tree("Pedro"),
                             tree("Miguel")
                             ),
                             tree("Tiene ojos verdes",
                                  tree("David"),
                                  tree("Andres")     
                                  )
                        ),
                        tree("Tiene camisa",
                        tree("Tiene corbata",
                              tree("Juan"),
                              tree("Lucas")
                              ),
                                tree("Tiene chaleco",
                                     tree("Mateo"),
                                     tree("Gerardo"))
                        )     
                    ),
                   tree("Es casada",
                        tree("Es mama",
                             tree("Es rubia",
                                  tree("Camila"),
                                  tree("Maria")
                                  )
                             ,
                             tree("Tiene canas",
                                  tree("Julia"),
                                  tree("Susana")
                                  )
                             ),
                            tree("Estudia",
                                 tree("Tiene ojos azules",
                                      tree("Lina"),
                                      tree("Marcela")
                                      ),
                                        tree("Trabaja",
                                             tree("Mercedes"),
                                             tree("Margarita")
                                             )
                         )
                   )
            )
        
                  
print busqueda_rec(arbol)