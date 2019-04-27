def pow(a, n):
    """
    Binary exponentiation uses the binary representation of the power.

    E.g.

    3^13 = 3^(1101)
         = 3^(8) + 3^(4) + 3^(1)

    Since a number n has exactly [logn] + 1 digits in base 2, we need to perform O(logn) multiplications




    :param a:
    :param n:
    :return:
    """
    result = 1
    while n > 0:
        if n & 1:
            result = result * a
        a = a * a
        n >>= 1
    return result


if __name__ == '__main__':
    print(pow(2, 4))