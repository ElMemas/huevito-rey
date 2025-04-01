def celsius_a_fahrenheit(celsius):
    """Convierte una temperatura de Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32

# Solicitar al usuario la temperatura en Celsius
temperatura_celsius = float(input("Introduce la temperatura en Celsius: "))

# Convertir a Fahrenheit
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)

# Mostrar el resultado
print(f"{temperatura_celsius}°C son {temperatura_fahrenheit}°F")
