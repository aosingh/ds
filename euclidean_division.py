
def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

if __name__ == '__main__':
    print(gcd(6, 4))