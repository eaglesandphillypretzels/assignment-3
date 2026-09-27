# This file is now called operations.py and contains basic arithmetic operations: addition, subtraction, multiplication, and division.
# Each operation is defined as a static method within the Operations class, allowing them to be called without creating an instance of the class.
class Operations:
    """
    This class contains static methods for basic arithmetic operations: addition, subtraction, multiplication, and division.
    Each method takes two float numbers as input and returns the result of the operation as a float.
    """

    @staticmethod
    def addition(a: float, b: float) -> float:
        """
        This static method takes two numbers (a and b) and returns their sum (a + b).
        The method is defined as static because it does not depend on any instance of the class; it can be called directly on the class itself.
        Example: if we call addition(5.0, 3.0), it will return 8.0.
        """
        return a + b

    @staticmethod
    def subtraction(a: float, b: float) -> float:
        """
        This static method takes two numbers (a and b) and returns their difference (a - b).
        Subtracting means we take one number and remove the value of the other number from it.
        Example: if we call subtraction(10.0, 4.0), it will return 6.0.
        """
        return a - b

    @staticmethod
    def multiplication(a: float, b: float) -> float:
        """
        This static method takes two numbers (a and b) and returns their product (a * b).
        Multiplying means we take one number and increase it by the other number’s value repeatedly.
        Example: if we call multiplication(2.0, 3.0), it will return 6.0.
        """
        return a * b

    @staticmethod
    def division(a: float, b: float) -> float:
        """
        This function takes two numbers (a and b) and returns their quotient (a / b).
        Dividing means breaking the first number into equal parts based on the second number.
        Raises ValueError when b is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
