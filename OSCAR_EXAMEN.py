def main():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    
    temp_max = max(temperaturas)
    temp_min = min(temperaturas)
    temp_promedio = sum(temperaturas) / len(temperaturas)
    
    print(f"Temperatura más alta: {temp_max}°C")
    print(f"Temperatura más baja: {temp_min}°C")
    print(f"Temperatura promedio: {temp_promedio:.2f}°C")

if __name__== "__main__":
    main()