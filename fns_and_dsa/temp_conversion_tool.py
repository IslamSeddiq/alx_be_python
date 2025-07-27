FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def is_valid_number(s):
    s = s.strip()
    return s.replace('.', '', 1).replace('-', '', 1).isdigit()

def main():
    temp_input = input("Enter the temperature to convert: ").strip()

    if not is_valid_number(temp_input):
        print("Invalid temperature. Please enter a numeric value.")
        return

    temperature = float(temp_input)

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "F":
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp:.2f}°C")
    elif unit == "C":
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp:.2f}°F")
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")

# Run the program
main()
