FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
temperature = int(input("Enter the temperature to convert: "))
Celsius_or_Fahrenheit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

def convert_to_celsius(fahrenheit):

    return fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR

if Celsius_or_Fahrenheit == "F":
    converted_temp = convert_to_celsius(temperature)
    print(f"{temperature}°F is {converted_temp}°C")
else:
    converted_temp = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {converted_temp}°F")
