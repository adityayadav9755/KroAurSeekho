def factorial_iterative(n):
    """

    :param n: Integer - jiska factorial chahiye
    :return: n! = n*(n-1)...1
    """
    fac = 1
    for i in range(n):
        fac = fac*(i+1)
    return fac


def factorial_recursion(n):
    """

    :param n: Integer - jiska factorial chahiye
    :return: n! = n*(n-1)...1
    """
    if n == 1:
        return 1
    else:
        return n*factorial_recursion(n-1)


x = int(input("Enter the number:"))
print(factorial_iterative(x))
print(factorial_recursion(x))
