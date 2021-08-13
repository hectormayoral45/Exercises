#Conversion decimal a binario
def getnum(): 
    numero = int(input("Ingrese numero "))
    return numero 

def bits(numero):
    for ind in range (0,10):
        if pow(2,ind) > numero:
            break
    return ind

valor = getnum() #Valor es el num a convertir
b = bits(valor)
print("Bits necesarios")
print(b)

#Potencia maxima de dos (Num de bits - 1)
potmax = pow(2,(b-1)) 
pos = 0 
binario = [] #Creacion de vector binario vacio
bandera = 0
suma = 0

def llenarceros(binario, b, potmax): 
        binario.insert(0,1)
        for inc in range(1,b):
            binario.insert(inc,0)
        return binario

def addone(binario):
    binario.insert(0, 1)
    bandera = 1
    return binario

def agregar1(binario,pos):
    binario.insert(pos,1)
    return binario

def rellenarcero(pos,binario,b):
    for count in range(pos,b):
        binario.insert(count,0)
    return binario


if potmax == valor:
    binario = llenarceros(binario, b, potmax)
    print(binario)
else: 
    if bandera == 0:
        binario = addone(binario)
        #print(binario)
        suma = pow(2,(b-1)) + pow(2,(b-2))
        #print(suma)
    for inc in range (1,b): 
        pos = inc
        if suma < valor: 
            print("Entro al for ")
            print (type(binario))
            binario = agregar1(binario,pos)
            suma = suma + pow(2,(pos+1))
            print(binario)
            print(suma)
        if suma == valor:
            print("Entro a rellenar")
            binario = rellenarcero(pos,binario,b)
            print(binario)
           
