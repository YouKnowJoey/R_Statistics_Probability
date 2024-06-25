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
    integral_result_0_to_y = integrate(f, (y, 0, y))
    print("The integral of f(y) from 0 to 'y' is:")
    print(integral_result_0_to_y)


print(integrate_piecewise())

def integrate_jpd():
    """Joint Probability Density Function integration"""
    # Define the variable
    x, y = symbols('x y')

    # Define the joint density function
    f = 24*x*y
    # Display the function
    print("The piecewise function f(y) is:")
    print(f)

    # Set up the integration
    integral_y = integrate(f, (y, 0, 1/2 - x))
    integral_x = integrate(integral_y, (x, 0, 1/2))
    print(integral_y)
    print(integral_x)

print(integrate_jpd())