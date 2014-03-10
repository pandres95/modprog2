from __future__ import print_function

def m_print(m, r_end = '\n', c_end = '\t'):
    for i in m:
        for j in i:
            print(j, end=c_end)
        print(end=r_end)

def Archivo(Dir):
    with open(Dir) as archivo:
        return [ [int(x) for x  in line if x !="\n"] for line in archivo ]

laberinto = (Archivo('prueba.txt'))

def borrarSol(sol, ultimo):
    if len(sol)==1: del sol[0]
    else:
        del sol[ultimo]
        borrarSol(sol, ultimo-1)

def arranque(lab,x):#Posicion de arranque en la matriz--> (X,0)
    return x if lab[x][0]==1 else arranque(lab,x+1)

def recorrido(lab,x,y,ax,ay,sol):#(x,y) pos actual (ax,ay) anterior casilla evaluada
    if(x<len(lab) or y<len(lab[0]) or x<0 or y<0):
        if   lab[x][y]!=2:      
            if continuar(lab,x,y,ax,ay):
                if x<ax:
                    if lab[x][y+1]!=0: return recorrido(lab,x,y+1,x,y, sol + ["Der"])
                    if lab[x-1][y]!=0: return recorrido(lab,x-1,y,x,y, sol + ["Arr"])
                    if lab[x][y-1]!=0: return recorrido(lab,x,y-1,x,y, sol + ["Izq"])
                if x>ax:
                    if lab[x][y+1]!=0: return recorrido(lab,x,y+1,x,y, sol + ["Der"])
                    if lab[x+1][y]!=0: return recorrido(lab,x+1,y,x,y, sol + ["Aba"])
                    if lab[x][y-1]!=0: return recorrido(lab,x,y-1,x,y, sol + ["Izq"])
                if y>ay:
                    if lab[x][y+1]!=0: return recorrido(lab,x,y+1,x,y, sol + ["Der"])
                    if lab[x-1][y]!=0: return recorrido(lab,x-1,y,x,y, sol + ["Arr"])
                    if lab[x+1][y]!=0: return recorrido(lab,x+1,y,x,y, sol + ["Aba"])
                if y<ay:
                    if lab[x][y-1]!=0: return recorrido(lab,x,y-1,x,y, sol + ["Izq"])
                    if lab[x-1][y]!=0: return recorrido(lab,x-1,y,x,y, sol + ["Arr"])
                    if lab[x+1][y]!=0: return recorrido(lab,x+1,y,x,y, sol + ["Aba"])
            else:
                borrarSol(sol, len(sol)-1)
                return recorrido([[0 if a == x and b == y else lab[a][b] for b in range(len(lab[0]))] for a in range(len(lab))],
                                  arranque(lab,0),0,arranque(lab,0)+1,0, sol)
        else: return sol + ["Ok"]

def xMenorax(m,n,lab): return lambda m,n: True if lab[m][n+1]!=0  or lab[m-1][n]!=0 or lab[m][n-1]!=0 else False
def xMayorax(m,n,lab): return lambda m,n: True if lab[m][n-1]!=0  or lab[m+1][n]!=0 or lab[m][n+1]!=0 else False
def yMenoray(m,n,lab): return lambda m,n: True if lab[m-1][n]!=0  or lab[m+1][n]!=0 or lab[m][n-1]!=0 else False
def yMayoray(m,n,lab): return lambda m,n: True if lab[m-1][n]!=0  or lab[m+1][n]!=0 or lab[m][n+1]!=0 else False

def continuar(lab,x,y,ax,ay): #(x,y) pos actual (ax,ay) anterior casilla evaluada
    if(x>=len(lab) or y>=len(lab[0]) or x<0 or y<0): return False
    if x<ax: return xMenorax(x,y,lab) 
    if x>ax: return xMayorax(x,y,lab) 
    if y<ay: return yMenoray(x,y,lab) 
    if y>ay: return yMayoray(x,y,lab) 
 
m_print(laberinto)
solucion = recorrido(laberinto,arranque(laberinto,0),0,arranque(laberinto,0)+1,0, [])
print (solucion[0:solucion.index('Ok')+1])