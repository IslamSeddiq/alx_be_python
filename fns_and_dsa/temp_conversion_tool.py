# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Conversion functions
def convert_to_celsius(fahrenheit: float):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius: float):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User interaction
def main():
    temp_input = input("Enter the temperature (e.g., 100F or 37C): ").strip().upper()

    try:
        if temp_input.endswith("F"):
            value = float(temp_input[:-1])
            celsius = convert_to_celsius(value)
            print(f"{value}°F is {celsius:.2f}°C")
        elif temp_input.endswith("C"):
            value = float(temp_input[:-1])
            fahrenheit = convert_to_fahrenheit(value)
            print(f"{value}°C is {fahrenheit:.2f}°F")
        else:
            raise ValueError("Invalid temperature unit. Please end with 'C' or 'F'.")
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value followed by 'C' or 'F'.")

# Run the program
main()
