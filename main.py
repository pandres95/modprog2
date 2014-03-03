from m_prints import *

def Archivo(Dir):
    with open(Dir) as archivo:
        return [ [int(x) for x  in line if x !="\n"] for line in archivo ]

def arranque(m, x, y):
    return (x, y) if m[x][y] == 1 else arranque(m, x+1, y)

def recorrido(m, i, f, v):
    return list(filter(lambda x: x is not None, \
                       list(map(lambda x: \
                                None if x+v >= len(m[0]) or x+v <= 0 else 
                                "Listo" if m[f][x+v] == 2 \
                                else "Gira izquierda" if m[f-1][x] == 1 \
                                else "Gira derecha"  if m[f+1][x] == 1 \
                                else "Retroceder"  if m[f][x+v] == 0 \
                                else "Avanzar" if m[f][x+v] == 1 \
                                else None, \
                            range(i, len(m[0])) if v > 0 else range(i, 0, -1))
                            )
                       )
                )


laberinto1 = [[0,0,0,0,0,0,0,0],
              [0,0,0,1,1,1,1,0],
              [1,1,1,1,2,0,0,0],
              [0,0,0,1,1,1,0,0],
              [0,0,0,0,0,1,2,0],
              [0,0,0,0,0,0,0,0]]



laberinto2 = (Archivo('prueba.txt'))

m_print(laberinto1)
print()
m_print(laberinto2, c_end='   ')
print(recorrido(laberinto2, 0, arranque(laberinto2, 0, 0)[0], 1))
