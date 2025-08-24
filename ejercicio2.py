def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_a_kelvin(celsius):
    return celsius + 273.15

def kelvin_a_celsius(kelvin):
    return kelvin - 273.15

# Menú para el usuario
print("=== Conversor de Temperatura ===")
print("1. Celsius a Fahrenheit")
print("2. Celsius a Kelvin")
print("3. Fahrenheit a Celsius")
print("4. Kelvin a Celsius")

opcion = input("Seleccione una opción (1/2/3/4): ")
valor = float(input("Ingrese la temperatura: "))

if opcion == "1":
    print(f"{valor}°C = {celsius_a_fahrenheit(valor)}°F")
elif opcion == "2":
    print(f"{valor}°C = {celsius_a_kelvin(valor)}K")
elif opcion == "3":
    print(f"{valor}°F = {fahrenheit_a_celsius(valor)}°C")
elif opcion == "4":
    print(f"{valor}K = {kelvin_a_celsius(valor)}°C")
else:
    print("Opción inválida")
