def divisores(n):
    return [x for x in range(1, n+1) if n % x == 0]

def m1tom10inv():
    return list(range(-1, -11, -1))

def suma(a, b):
    return a + b

def sumaListas(a, b):
    return list(map(suma, a, b))

def iniciales(w):
    return [p[0] for p in w]

def buscarFin(w, c):
    return [p for p in w if p[-1] == c] if c in ['a', 'e', 'i', 'o', 'u'] else []

a = [1, 2, 3]
b = [4, 5, 6]
w = ["patata", "lel", "what", "lola"]

print()
print("a = ", a)
print("b = ", b)
print("w = ", w)
print()

print("divisores 15\t", divisores(15))
print("m1tom10inv\t", m1tom10inv())
print("sumaListas a b\t", sumaListas(a, b))
print("iniciales w\t", iniciales(w))
print("buscarFin w 'a'\t", buscarFin(w, 'a'))
 
