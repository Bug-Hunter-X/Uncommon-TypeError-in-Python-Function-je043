def improved_function_with_error_handling(a, b):
    try:
        if isinstance(b, (int, float)) and b != 0:
            result = a / b
            return result
        elif not isinstance(b,(int, float)):
            raise TypeError("Invalid input type. Divisor must be a number.")
        else:
            raise ZeroDivisionError("Division by zero")
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError as e:
        return str(e)

#More robust error handling in this version
print(improved_function_with_error_handling(5, "hello"))
print(improved_function_with_error_handling(5, 0))
print(improved_function_with_error_handling(5, 2))
print(improved_function_with_error_handling(5, [1,2,3]))