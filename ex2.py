#Conversion decimal a binario
numero = int(input("Ingrese numero "))

def bits(numero):
    for ind in range (0,10):
        if pow(2,ind) > numero:
            break
    return ind


pot = bits(numero)
print (pot)
power = pot - 1 #Potencia maxima de dos

binario = []

#def convert(pot):

temp = pow(2,power)
print(temp)
#def completo(temp , binario, pot):
if temp == numero: #Esta condicion debe ir en codigo main
    binario.insert(0,1)
    for inc in range(1,pot):
        binario.insert(inc,0)
elif temp != numero: 
#def ad1(binario,temp, power):
    ban = 0
    band = 0
    if band == 0:
        binario.insert(0,1) #Asumes que requieres el MSB
        ban = 1             #No agregar MSB 
    print("No es igual")
    pos = 1
    while temp < numero or ban==0:
            temp = temp + pow(2,(power-pos))
            print(f"temporal es ",temp)
            binario.insert(pos,1)
            pos = pos + 1
            if pos == power:
                ban = 1
            
    #if temp < numero

print(binario)

