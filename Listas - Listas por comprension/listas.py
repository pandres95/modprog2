#######################################################
def sumar(l):
    return l[0] if len(l) == 1 else l[0] + sumar(l[1::])

def invertir(l):
    return [] if len(l) == 0 else invertir(l[1::]) + [l[0]]

def igualLista(a, b):
    return (False if len(a) != len(b) else True if (len(a) == 0 and len(b) == 0) else a[0] == b[0] and igualLista(a[1::], b[1::]))

def lista_ordenada(l):
    return True if len(l) == 0 else True if len(l) == 1 else l[0] < l[1] and lista_ordenada(l[1::])

def mostrar_ubicacion(l, n):
    return l[0] if n == 0 else mostrar_ubicacion(l[1::], n - 1) 

def mayor(l):
    return 0 if len(l) == 0 else l[0] if l[0] > mayor(l[1::]) else mayor(l[1::])

def contarpares(l):
    return 0 if len(l) == 0 else 1 + contarpares(l[1::]) if l[0] % 2 == 0 else 0 + contarpares(l[1::])

def cuadrados(l):
    return [] if len(l) == 0 else [l[0]*l[0]] + cuadrados(l[1::])

def divisible(x, y):
    return x % y == 0

def divisibles(x):
    return [y for y in range(1,x+1) if divisible(x, y)]

def esPrimo(x):
    return len(divisibles(x)) <= 2

def primos(x):
    return [y for y in range(1, x) if esPrimo(y)]

#######################################################

def head(l):
    return l[0]

def tail(l):
    return l[1::]

def init(l):
    return invertir(tail(invertir(l)))

def last(l):
    return head(l) if len(l) == 1 else last(tail(l))

def lenght(l):
    return len(l)

def take(n, l):
    return [head(l)] if n == 1 else [head(l)] + take(n-1, tail(l))

def drop(n, l):
    return invertir(init(invertir(l))) if n == 1 else drop(n-1, invertir(init(invertir(l))))

def takeWhile(cond, l):
    return [x for x in l if eval('x ' + cond)]

def dropWhile(cond, l):
    return [x for x in l if not eval('x ' + cond)]

def reverse(l):
    return invertir(l)

def concat(l):
    return sumar(l)

def words(s):
    return [y for y in s.split(' ') if y != '']

def unwords(l):
    return head(l) if lenght(l) == 1 else head(l) + " " + unwords(tail(l))

def elem(e, l):
    return e in l

def notElem(e, l):
    return not elem(e, l)

#######################################################

a = [i+1 for i in range(10)]
b = list(range(0,20,2))
c = ["open", "source", "solutions"]
w = " I like to use Microsoft Windows"
print()
print('a = ', a)
print('b = ', b)
print('c = ', c)
print('w =  "%s"' % w)
print()

print('sumar a\t\t\t\t', sumar(a))
print('invertir a\t\t\t', invertir(a))
print('igualLista a a\t\t\t', igualLista(a, a))
print('igualLista a b\t\t\t', igualLista(a, b))
print('lista_ordenada a\t\t', lista_ordenada(a))
print('lista_ordenada invertir a\t', lista_ordenada(invertir(a)))
print('mostrar_ubicacion b 5\t\t', mostrar_ubicacion(b, 5))
print('mayor b\t\t\t\t', mayor(b))
print('contarpares a\t\t\t', contarpares(a))
print('cuadrados a\t\t\t', cuadrados(a))
print('esPrimo 2\t\t\t', esPrimo(2))
print('esPrimo 6\t\t\t', esPrimo(6))
print('primos 100\t\t\t', primos(100))
print()

print('a!!2\t\t\t\t', mostrar_ubicacion(a, 2))
print('head a\t\t\t\t', head(a))
print('last a\t\t\t\t', last(a))
print('tail a\t\t\t\t', tail(a))
print('init a\t\t\t\t', init(a))
print('lenght a\t\t\t', lenght(a))
print('take 2 a\t\t\t', take(2, a))
print('drop 2 a\t\t\t', drop(2, a))
print('takeWhile (<=15) b\t\t', takeWhile('<=15', b))
print('dropWhile (<=15) b\t\t', dropWhile('<=15', b))
print('reverse a\t\t\t', reverse(a))
print('concat c\t\t\t "%s"' % concat(c))
print('words w\t\t\t\t', words(w))
print('unwords words w\t\t\t', unwords(words(w)))
print('elem 3 b\t\t\t', elem(3, b))
print('notElem 3 b\t\t\t', notElem(3, b))
