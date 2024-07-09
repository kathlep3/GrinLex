
class Arithmetic:
    """class for math functions"""
    def add(self, value, operand):
        """handles addition operation"""
        try:
            if isinstance(value, str) and isinstance(operand, str):
                result = value + operand
            else:
                result = value + operand
            return result
        except TypeError as e:
            print(e, "Invalid values for addition.")

    def sub(self, value, operand):
        """handles subtraction operation"""
        try:
            result = value - operand
            return result
        except TypeError as e:
            print(e, "Invalid values for subtraction")

    def mult(self, value, operand):
        """handles multiplication operation"""
        try:
            if isinstance(value, str) and isinstance(operand, int):
                result = value * operand
            elif isinstance(value, int) and isinstance(operand, str):
                result = value * operand
            else:
                result = value * operand
            return result
        except TypeError as e:
            print(e, "Invalid values for multiplication")

    def div(self, value, operand):
        """handles division operation"""
        try:
            result = value/operand
            if isinstance(value, int) and isinstance(operand, int):
                result = int(result)
            return result
        except TypeError as e:
            print(e, "Invalid values for division")
        except ZeroDivisionError as e:
            print(e, "Invalid values for division.")
