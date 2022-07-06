import sys


def catalan(n):
    return 1 if n <= 1 else sum(catalan(i) * catalan(n - i - 1) for i in range(n))


if __name__ == "__main__" and len(sys.argv) > 1:
    a = int(sys.argv[1])
    print(catalan(a))
