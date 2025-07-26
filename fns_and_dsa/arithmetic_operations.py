def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs an arithmetic operation on two numbers.

    Parameters:
    - num1 (float): The first number.
    - num2 (float): The second number.
    - operation (str): The operation to perform: 'add', 'subtract', 'multiply', 'divide'.

    Returns:
    - float: Result of the arithmetic operation.
    - str: Error message if division by zero or invalid operation.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "ERROR_DIVISION_BY_ZERO"
        return num1 / num2
    else:
        return "ERROR_INVALID_OPERATION"
