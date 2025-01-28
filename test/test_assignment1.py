import math

def babylonian_method(s, a, error_tol, max_iter):
    """
    Babylonian approximation method for finding square roots.

    :param s: The number the user wants to find the square root of.
    :param a: The initial approximation.
    :param error_tol: The accepted error tolerance.
    :param max_iter: The maximum number of iterations.
    
    :return: The error, number of iterations, and the approximation.
    """
    i=0
    error = abs(a-(s**(1/2)))

    while error > error_tol:
        a=(a + (s/a))/2
        error = abs(a-(s**(1/2)))
        i += 1
        if i >= max_iter:
            print("Method Failed. Max number of iterations reached.")
            quit()
    print(f"The error is {error}")
    print(f"The number of iterations is {i}")
    print(f"The approximation is {a}")

#Example to make sure it works
#babylonian_method(2,2,0.0001,100)


def bisection_method(func, a, b, error_tol, max_iter):
    """
    Parameters:

    :param func: The user defined function.
    :param a: The initial lower boundary.
    :param b: The initial upper boundary.
    :param error_tol: The accepted error tolerance.
    :param max_iter: The max number of iterations.

    Returns:

    :return: The boundaries and error at the final iteration, and also the number of iterations.
    """

    i = 0
    def f(x):
        f = eval(func)
        return f

    error = abs(b-a)

    while error > error_tol:
        c = (b+a) / 2

        if f(a) * f(b) >= 0:
            print("No/Multiple Roots Present. Bisection method will not work")
            quit()

        elif f(c) * f(a) < 0:
            b = c
            error = abs(b-a)
            i += 1

        elif f(c) * f(b) < 0:
            a = c
            error = abs(b-a)
            i += 1

        elif i >= max_iter:
            print("Method failed. Max number of iterations reached.")
            quit()

        else:
            print("Something went wrong.")
            quit()

    print(f"The error is {error}")
    print(f"The lower boundary is {a} and the upper boundary is {b}")
    print(f"Number of iterations is {i}")

# Example to make sure it works.
#bisection_method("(4*x ** 3) + 3*x - 3", 0, 1, 0.01, 100)

def fixed_point_iteration(func, a, error_tol, max_iter):
    """

    :param func: The user defined function representing g(x) in x = g(x)
    :param a: The users initial approximation.
    :param error_tol: The accepted error tolerance.
    :param max_iter: The maximum number of iterations

    :return: The error, number of iterations, and approximation.
    """
    i=0

    def f(x):
        f = eval(func)
        return f

    #error = abs(a-f(a))

    while i <= max_iter:
        i+=1
        a_new = f(a)
        error = abs(a_new-a)
        if abs(a_new-a) < error_tol:
            print(f"The error is {abs(a_new-a)}")
            print(f"The number of iterations is {i}")
            print(f"The approximation is {a_new}")
            quit()
        a = a_new

    print("Method Failed. Maximum number of iterations reached.")

#Example to make sure it works
#fixed_point_iteration("((x**2) - 1)/3", 2, 0.1, 100)

def newtons_method(func, prime, x, n, error_tol):
    """

    :param func: Function given by the user.
    :param prime: Derivative of func, given by the user.
    :param x: The users initial estimate for the root.
    :param n: The maximum number of iterations.
    :param error_tol: The accepted error tolerance.
    :return:
    """
    def f(x):
        f = eval(func)
        return f
    def df(x):
        df = eval(prime)
        return df

    intercept = 1

    for intercept in range(1,n):
        i = x - (f(x)/df(x))
        if abs(i-x) < error_tol:
            print(f"The root was found at {x} after {intercept} iterations")
            print(f"The error is {abs(i-x)}")
            quit()
        else:
            x=i


    print(f"Method failed. Maximum number of iterations reached.")

# Example to make sure it works.
#newtons_method("x**2 - 2", "2*x", 2, 1, 0.01)
