"""File: sum_fractions.py

Author: Tyler Johnson
Date completed: 05/15/23

Description:
    learn to check modules with doctest
"""


def add_fractions(x, y):
    """returns the sum of two fractions (as a fraction in tuple format)

        Args:
        x (tuple): first fraction in the format (numerator, denominator)
        y (tuple): second fraction in the format (numerator, denominator)

        Return:
        tuple_sum (tuple): fraction in the format (numerator, denominator)

        Example:
        >>> add_fractions((3,5),(4,7))
        (41, 35)
    """
    n_x=x[0] # first numerator 
    d_x=x[1] # first denominator
    n_y=y[0] # second numerator
    d_y=y[1] # second denominator

    tuple_sum = ((n_x * d_y) + (n_y * d_x) ,  (d_x * d_y))
    return tuple_sum

m = (5,3)
n = (7,4)

print (add_fractions(m,n))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)