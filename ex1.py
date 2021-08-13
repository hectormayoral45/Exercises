#Ejercicio de tarea 1

numero = int(input("Ingrese numero "))

#Funcion para obtener el numero de bits necesarios
def bits(numero): 
    for leng in range(0,10):
        if numero < pow(2,leng-1):
            break
    return leng

                    
lenh = bits(numero)

def create (lenh): 
    count = 0
    binario = []
    for count in range(0,lenh):
        binario.append(0)
        print(binario[count])
    return binario
            
print(f"Bits necesarios ",{lenh})
bin = create(lenh)


def conver(numero,lenh,bin):
    if pow(2,lenh-1) == numero:
            bin[0]="1"
            print("Bin es ")
            print(bin)
            #break
    else:
        for ind in range (0,lenh):
            comp = pow(2,lenh-2-ind)
            if comp < numero:
                comp = 0
                bin[ind]="1"
                comp = comp + pow(2,lenh-2-ind)
                print(f"Comp es igual a ",{comp})
            elif comp > numero:
                bin[ind]="0"
                comp=0
    return bin

#print(bin)
numer = conver(numero, lenh, bin)
print(numer)
#inv = list(reversed(numer))
#print(inv)
print(range(0,lenh))



