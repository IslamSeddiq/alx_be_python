num1 = float(input("Enter the furst number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        print(f"The addition = {num1 + num2}")
    case "-":
        print(f"The subtraction = {num1 - num2}")
    case "*":
        print(f"The multiplication = {num1 * num2}")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print(f"The division = {num1 / num2}")
    case _:
        print("Invalid input")