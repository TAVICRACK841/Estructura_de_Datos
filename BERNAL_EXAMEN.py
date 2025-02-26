def decimal_a_binario(n):
   
    if n == 0:
        return '0'
   
    elif n == 1:
        return '1'
    else:
       
        return decimal_a_binario(n // 2) + str(n % 2)


numero = int(input("Ingresa un número entero positivo: "))


if numero < 0:
    print("Por favor, ingresa un número entero positivo.")
else:
    
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")