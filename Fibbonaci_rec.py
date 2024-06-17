def fib(n, a, b):  # My way
    """

    :param n: Integer
    :param a: Integer
    :param b: Integer
    :return: nth term of Fibonacci Series
    """
    if n == 1:
        return a
    else:
        return fib(n-1, b, a+b)


def fib1(n):  # Harry bhai's way
    """

    :param n: Integer
    :return: nth term of Fibonacci Series
    """
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)


x = int(input("Enter the position:"))
print(fib(x, 0, 1))
print(fib1(x))
