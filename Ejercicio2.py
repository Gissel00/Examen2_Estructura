ops = ['+','d','c']
arreglo = []
Pedirdatos = True

def OPS():
    return input("Ingrese una operacion :\n Entero= agregar  \n + = suma, \n d = duplicar, \n c = eliminar dato anterior, \n s = salir \n")


def Search(n, elementps):
    for i in range (len(n)):
        if n[i] == elementps:
            return True
    return False



while Pedirdatos == True:
    operacion = OPS()

    numero = operacion.isnumeric()

    if numero == True:
        arreglo.append(operacion)
        print('Agregago')
    else:
        if operacion == 'S' or operacion == 's':
            Pedirdatos = False
        else:

            operacionValida =Search(ops, operacion)

            if len(arreglo) > 0 and ops:
                arreglo.append(operacion)
                print('Agrehado')
            else:
                print('No se agregp')
print(arreglo)


total = 0
ant = 0
anuevo = []

for numer in arreglo:
    esnum = numer.isnumeric()

    if esnum == True:
        anuevo.append(numer)
        ant = numer;
    elif numer == '+':
        leng = len(anuevo)
        anuevo.append(int(anuevo[leng -1]) + int(anuevo[leng -2]))
    elif numer == 'c':
        leng = len(anuevo)
        anuevo.pop()
    elif numer == 'd':
        leng = len(anuevo)
        anuevo.append(int(anuevo[leng -1]) * 2)
    

print(anuevo)

for elemento in anuevo:
    total += int(elemento)

print(total)