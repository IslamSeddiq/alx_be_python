def perform_operation():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    match operation:
        case "add":
            print(num1 + num2)
        case "subtract":
            print(num1 - num2)
        case "multiply":
            print(num1 * num2)
        case "divide":
            if num2 == 0:
                print("Cannot be divided by 0")
            else:
                print(num1 / num2)

perform_operation()