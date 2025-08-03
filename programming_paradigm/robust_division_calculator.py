# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."


# main.py

import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        return

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    
    if isinstance(result, float):
        print(f"The result of the division is {result}")
    else:
        print(result)

if __name__ == "__main__":
    main()


