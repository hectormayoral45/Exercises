b =1 
while b==1:

    numero = int(input("Ingrese numero "))

    for ind in range (0,10):
        if pow(2,ind) > numero:
            break

    print("Numero de bits")
    print(ind)
    binario = []

    for count in range (0, ind):    
        mod = int(numero % 2)
        numero = (numero-mod) / 2 
        binario.append(mod)
    
    binario2 = list(reversed(binario))
    print(f"Numero binario ",binario2)
    print(f"Numero binario revertido",binario)

    decimal =0
    potmax = ind-1
    for im in range(0, ind):
        decimal = decimal + binario[im] * pow(2, (potmax-im))

    print(decimal)