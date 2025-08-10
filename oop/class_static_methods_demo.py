class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static Method
    @staticmethod
    def add(a, b):
        return a + b

    # Class Method
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Demo usage
if __name__ == "__main__":
    # Using static method
    sum_result = Calculator.add(5, 3)
    print(f"The sum is: {sum_result}")

    # Using class method
    product_result = Calculator.multiply(4, 6)
    print(f"The product is: {product_result}")

