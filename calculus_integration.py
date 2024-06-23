from sympy import symbols, exp, Piecewise, integrate, oo


def definite_integral_example():
    # Define the variables
    y, b = symbols('y b')

    # Define the function
    f = 5 / (8 * b)

    # Define the limits
    lower_limit = (2 * b) / 5
    upper_limit = y

    # Compute the definite integral
    definite_integral = integrate(f, (y, lower_limit, upper_limit))
    print("The definite integral of", f, "from", lower_limit, "to", upper_limit, "is", definite_integral)

def integrate_piecewise():
    # Define the variable
    y = symbols('y')

    # Define the piecewise function
    f = Piecewise((1/4 * exp(-y/4), y >= 0), (0, True))

    # Display the function
    print("The piecewise function f(y) is:")
    print(f)

    # Example: Integrate from 0 to infinity (which should equal 1 for a properly normalized PDF)
    integral_result_0_to_inf = integrate(f, (y, 0, y))
    print("The integral of f(y) from 0 to infinity is:")
    print(integral_result_0_to_inf)


print(integrate_piecewise())
