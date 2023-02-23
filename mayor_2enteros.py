# prgrama para verificar cual de dos numeros enteros es el mayor

print("----------------------------------------")
print("-------------ENTERO MAYOR---------------")
print("----------------------------------------")

# input
X = int(input("Digite el valor de x: "))
y = int(input("Digite el valor de y:"))

# processing
if X == y:
    print("Los numeros son iguales...")

else:
    if X > y:
        mayor = X
    else:
        mayor = y
        print("El mayor entre" + str(X) + " y " + str(y) + " es " + str(mayor))    
 
#output
print("----------------------------------------")
print("--------------RESULTADOS----------------")
print("----------------------------------------")
print("EL MAYOR ENTRE: " + str(X) + " y " + str(y) + " es " + str(mayor))