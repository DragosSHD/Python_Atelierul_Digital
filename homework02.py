# Adder function
def my_adder_func(*params, **kwargs):
    crt_sum = 0
    # Iterate through the parameter list.
    for i in params:
        # Check if the parameter is a number (integer or real) and then add it to the sum.
        if isinstance(i, (int, float)):
            crt_sum += i
    # Return the result
    return crt_sum


# Recursive Gauss sum function
def my_recursive_function(crt_in, *params):
    if params:
        crt_parity = params[0]
        if crt_parity == 'even':
            if crt_in % 2 != 0:
                crt_in -= 1
        elif crt_parity == 'odd':
            if crt_in % 2 == 0:
                crt_in -= 1
        return crt_in + my_recursive_function(crt_in - 2, crt_parity) if crt_in > 0 else 0

    return crt_in + my_recursive_function(crt_in - 1) if crt_in > 0 else 0


# Check integer function
def check_integer(in_var):
    return in_var if isinstance(in_var, int) else 0


# Test the adder function:
print(my_adder_func(1, 5, -3, 'abc', [12, 56, 'cad']))
print(my_adder_func())
print(my_adder_func(2, 4, 'abc', param_1=2))

print()

# Test the recursive function:
print(my_recursive_function(5))
print(my_recursive_function(5, 'odd'))
print(my_recursive_function(5, 'even'))

print()

# Test the function that checks for integer:
print(check_integer(21))
print(check_integer("A String"))
print(check_integer(23.42))
