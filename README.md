# cot-4500-Pro1
There are no requirements other than pip and base python. I'm not sure why numpy is in my requirements.txt file, it isnt used in my program. I tried to make this so no extra packages are necessary to get everything to work, although you might want to use the math module that comes with python to use trig functions. I imported it in my main .py files but it didn't sync to the requirements.txt for some reason.

I'm not sure what __init__.py is supposed to be.

The main meat of the assignment is in the form of four functions. To run any of my algorithms, open the main or test file in pycharm then add a new line calling the function and setting the parameters. In the files I included a (commented out) example with each one of the functions. It would look like this: newtons_method("x**2 - 2", "2*x", 2, 1, 0.01)

Also included in the main files are lists of each parameter and its purpose. They are directly under where I start to define the function and look like this:  
    """
    :param func: Function given by the user.
    :param prime: Derivative of func, given by the user.
    :param x: The users initial estimate for the root.
    :param n: The maximum number of iterations.
    :param error_tol: The accepted error tolerance.
    :return:
    """
