import random

baraja = [["A",1],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1],[8,1],[9,1],["J",1],["Q",1],["K",1],
          ["A",2],[2,2],[3,2],[4,2],[5,2],[6,2],[7,2],[8,2],[9,2],["J",2],["Q",2],["K",2],
          ["A",3],[2,3],[3,3],[4,3],[5,3],[6,3],[7,3],[8,3],[9,2],["J",3],["Q",3],["K",3],
          ["A",4],[2,4],[3,4],[4,4],[5,4],[6,4],[7,4],[8,4],[9,2],["J",4],["Q",4],["K",4]]

def meter(card):
    baraja.insert(0, card)

def sacar():
    return baraja.pop()

def vacio():
    return tam() == 0

def tam():
    return len(baraja)

##########################
def crea_baraja():
    random.shuffle(baraja)

crea_baraja()
##########################

def desc(card):
    if(card == None):
        return "Nada"
    if card[1] == 1:
        return str(card[0]) + " de picas"
    elif card[1] == 2:
        return str(card[0]) + " de corazones"
    elif card[1] == 3:
        return str(card[0]) + " de diamantes"
    elif card[1] == 4:
        return str(card[0]) + " de treboles"

def i_mano(a, b, c):
    print('%s, %s, %s' % (desc(a), desc(b), desc(c)))

def cambio_mano(a, b, c, n, o):
    if(o == 1):
        meter(a)
        return trios(list(sacar()), b, c, n)
    elif(o == 2):
        meter(b)
        return trios(a, list(sacar()), c, n)
    elif(o == 3):
        meter(c)
        return trios(a, b, list(sacar()), n)
  
def trios(a, b, c, n):
    
    if(a == None and b == None and c == None):
        print('Bienvenido a Trios. Vamos a jugar')
        print('*********************************')
        trios(list(sacar()), b, c, n+1)
    else:
        print('Tu mano es:', end=' ')
        i_mano(a, b, c)
    
        if(a == None):
            return trios(list(sacar()), b, c, n+1)
        elif(b == None):
            return trios(a, list(sacar()), c, n+1)
        elif(c == None):
            return trios(a, b, list(sacar()), n+1)
        
        if(a != None and b != None and c != None):
            if(n > 4):
               return (a, b, c)
            else:
                while(not((a[0] == b[0] and b[0] == c[0]) or (a[1] == b[1] and b[1] == c[1]))):
                    #cambio_mano(a, b, c, n+1, int(input("Que carta quieres cambiar? [1, 2 o 3]: "))) #No funciona. Tiene un comportamiento no esperado
                    (a, b, c) = cambio_mano(a, b, c, n+1, int(input("Que carta quieres cambiar? [1, 2 o 3]: ")))
            print('Felicitaciones, has conseguido el siguiente trio')
            i_mano(a, b, c)
            return


trios(None, None, None, 1)
