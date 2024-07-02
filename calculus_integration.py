from sympy import symbols, exp, Piecewise, integrate, oo
import sympy as sp


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


def integrate_for_expected_value():
    """Integration for mean (expected value)"""
    # Define the variable
    y = symbols('y')

    # Define the probability density function add a 'y'
    f = 5*(1-y)**4
    # Display the function
    print("The pdf function f(y) is:")
    print(f)

    # Set up the integration
    integral_y = integrate(f, (y, (1/6), 1))
    print(integral_y)

def normal_distribution_integration():
    # Define the variables and parameters
    mu = 40  # Mean
    sigma = 6.3  # Standard deviation
    lower_bound = 32  # Given lower bound

    # Define the normal distribution variable and integration limits
    x = symbols('x')
    normal_distribution = 1 / (sigma * sp.sqrt(2 * sp.pi)) * sp.exp(-(x - mu)**2 / (2 * sigma**2))
    lower_limit = lower_bound

    # Perform the integration
    probability_more_than_32 = sp.integrate(normal_distribution, (x, lower_limit, sp.oo))

    # Print the result
    print("Probability that a mouse will live more than 32 months:")
    print(probability_more_than_32.evalf())  # Use evalf() to evaluate the numerical result

def normal_distribution_integration_two():
    # Define the variables and parameters
    mu = 40  # Mean
    sigma = 6.3  # Standard deviation
    lower_bound = 37  # Given lower bound
    upper_bound = 49 # Given upper bound

    # Define the normal distribution variable and integration limits
    x = symbols('x')
    normal_distribution = 1 / (sigma * sp.sqrt(2 * sp.pi)) * sp.exp(-(x - mu)**2 / (2 * sigma**2))
    lower_limit = lower_bound

    # Perform the integration
    probability_between_37_49 = sp.integrate(normal_distribution, (x, lower_limit, upper_bound))

    # Print the result
    print("Probability that a mouse will live between 37 and 49 months:")
    print(probability_between_37_49.evalf())  # Use evalf() to evaluate the numerical result

print(normal_distribution_integration_two())
