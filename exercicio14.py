"""
Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.
"""

tempCelsius = float(input("Digite a temperatura em Celsius: "))

tempFahrenheit = ((9 * tempCelsius ) / 5) + 32
tempKelvin = tempCelsius + 273.15

print(f"A temperatura {tempCelsius} ºC corresponde a {tempFahrenheit} ºF e {tempKelvin} K.")