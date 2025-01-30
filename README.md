# Requirements

There are no requirements other than pip and base python, but pycharm is reccomended. I dont know why numpy is in my requirements.txt file, it isnt used in my program. I tried to make this so no extra packages are needed, but you might want to use the math module that comes with python for trig functions. I imported it in my main .py files but it didn't sync to the requirements.txt for some reason.

# How to use

To run any of the algorithms, open the main or test file in pycharm then add a new line on bottom calling the function and setting the parameters and run the program. After you call a function, comment it out before calling the next. 



In the files I included a (commented out) example with each one of the functions. It would look like this: 
    
    newtons_method("x**2 - 2", "2*x", 2, 1, 0.01)

Also included in the main files are lists of each parameter and its purpose. They are directly under where I start to define the function and look like this:  

    """
    :param func: Function given by the user.
    :param prime: Derivative of func, given by the user.
    :param x: The users initial estimate for the root.
    :param n: The maximum number of iterations.
    :param error_tol: The accepted error tolerance.
    :return:
    """
Ignore the test branch that was from before I learned how to make github folders.
