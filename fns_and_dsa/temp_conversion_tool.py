FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit temperature to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Get user input
        temp_input = input("Enter the temperature (e.g., '32F' or '100C'): ").strip().upper()
        
        # Extract numerical value and unit
        if temp_input[-1] == 'C':
            celsius = float(temp_input[:-1])
            fahrenheit = convert_to_fahrenheit(celsius)
            print(f"{celsius}°C is {fahrenheit:.2f}°F")
        elif temp_input[-1] == 'F':
            fahrenheit = float(temp_input[:-1])
            celsius = convert_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is {celsius:.2f}°C")
        else:
            raise ValueError("Invalid temperature format. Please use 'C' or 'F' (e.g., '32F' or '100C').")
    
    except ValueError as e:
        if "could not convert string to float" in str(e):
            print("Invalid temperature. Please enter a numeric value.")
        else:
            print(e)

if __name__ == "__main__":
    main()
