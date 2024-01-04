def factorial(n):
    if n < 0:
        raise ValueError("n must be a positive integer")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    n = 5
    print("5! =", factorial(n))  # output 5!=120
