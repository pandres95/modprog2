from __future__ import print_function

class tree:
    def __init__(self, val = None, arboles = []):
        self.valor = val
        self.hijos = arboles

    def __str__(self):
        return "(" + "(" + str(self.valor) + ")" \
                    + (
                       reduce(lambda x, y: x + str(y), self.hijos[1::], str(self.hijos[0])) 
                       if self.hijos != [] else ""
                       ) \
                + ")"
              
                
clue = tree(1,
            [
             tree(2,
                  [
                   tree(4),
                   tree(6),
                   tree(8),
                   tree(10,
                        [
                         tree(20),
                         tree(40),
                         tree(60)
                         ]
                        )
                   ]
                  ),
             tree(3,
                  [
                   tree(9),
                   tree(12),
                   tree(27)
                   ]
                  ),
             tree(5,
                  [
                   tree(30),
                   tree(15),
                   tree(25),
                   tree(100,
                        [
                         tree(300),
                         tree(500)
                         ]
                        )
                   ]
                  )
            ]
        )

   
def i_hojas(nodo):
    print ([hoja.valor for hoja in nodo.hijos])
    
def suma_hijos(nodo):
    if(nodo.hijos == []):
        return nodo.valor
    else:
        return nodo.valor + reduce(lambda x, y: x + suma_hijos(y), nodo.hijos[1::], nodo.hijos[0].valor)

def imprimir_hijos_valor(nodo, valor):
    if buscar_hijo_valor(nodo, valor) != None:
        x = buscar_hijo_valor(nodo, valor)
        print(x) 
    else:
        print(None)

def buscar_hijo_valor(nodo, valor):
    
    if nodo.valor == valor:
        return nodo
    else:
        if len(filter(lambda x: x != None,
                      [
                       buscar_hijo_valor(hijo, valor) 
                       for hijo in filter(lambda x: valor % x.valor == 0, nodo.hijos)
                       ]
                      )) != 0:
            return filter(lambda x: x != None,
                      [
                       buscar_hijo_valor(hijo, valor) 
                       for hijo in filter(lambda x: valor % x.valor == 0, nodo.hijos)
                       ]
                      )[0]
        else:
            return None
def insertar(arbol,num):
    if len([x for x in arbol.hijos if num%x.valor==0])==0:
        return tree(arbol.valor,arbol.hijos+[tree(num)])
    else:
        return tree(arbol.valor,insertarhijos(arbol.hijos,num))
         
         
def insertarhijos(lista,num):
    if  (num%lista[0].valor==0):
        return [insertar(lista[0],num)]+lista[1:]
    else:
        return [lista[0]]+insertarhijos(lista[1:],num)
                
#Imprimir arbol    
print(clue,'\n')
#impimir hijos de un nodo
imprimir_hijos_valor(clue, 10)
#insertar nodo
clue=insertar(clue,18)
#suma de subnodos a partir de un nodo
print (suma_hijos(clue))
