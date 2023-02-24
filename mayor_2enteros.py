# prgrama para verificar cual de dos numeros enteros es el mayor

print("----------------------------------------")
print("-------------ENTERO MAYOR---------------")
print("----------------------------------------")

# input
x = int(input("Digite el valor de x: "))
y = int(input("Digite el valor de y:"))

# processing
if x == y:
    # output
    print("Los numeros son iguales...")
else:
    if x > y:
        mayor = x
    else:
        mayor = y  
        # output
    print("----------------------------------------")
    print("--------------RESULTADOS----------------")
    print("----------------------------------------")
    print("EL MAYOR ENTRE: " + str(x) + " y " + str(y) + " es " + str(mayor))