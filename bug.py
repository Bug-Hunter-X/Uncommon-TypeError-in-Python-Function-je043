def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Invalid input type"

# This call will raise a TypeError because a string is passed
print(function_with_uncommon_error(5, "hello"))

# This call will raise a ZeroDivisionError
print(function_with_uncommon_error(5, 0))

# This is a type error which might be caught unexpectedly.
print(function_with_uncommon_error(5, [1,2,3]))