'''
Metodo da Bisseção 
'''
import math
opcao = input("Metodo: ")
if opcao == "B":
    ak = float(input('a: '))
    bk = float(input('b: '))
    E1 = float(input('e1: '))
    E2 = float(input('e2: '))
    def func(x):
        f = ((2**x)-(3*x)) #Insira a função do exercicio aqui#
        return f
    while True:
        xk = (ak+bk)/2
        poten1 = (ak-bk)**2
        module1 = math.sqrt(poten1)
        poten2 = (func(xk))**2
        module2 = math.sqrt(poten2)
        if module1 < E1 or module2 < E2:
            break
        fp = func(xk)
        fa = func(ak)
        if fp*fa > 0:
            ak = xk
        else:
            bk = xk
    

print('[',ak,',',bk,']')
