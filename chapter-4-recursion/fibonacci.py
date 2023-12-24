num_call_bad = 0
num_call_good = 0


def bad_fibonacci(n):
    global num_call_bad
    num_call_bad += 1
    if n < 2:
        return n
    return bad_fibonacci(n - 1) + bad_fibonacci(n - 2)


def good_fibonacci(n):
    global num_call_good
    num_call_good += 1
    if n < 2:
        return n, 0
    a, b = good_fibonacci(n - 1)
    return a+b, a


if __name__ == '__main__':
    n = 15
    print(f"Bad fibonacci:\nF({n}) = F({n - 1}) + F({n - 2}) = ", bad_fibonacci(n))
    print("number of calls: ", num_call_bad)
    print(f"Good fibonacci:\nF({n}) = F({n - 1}) + F({n - 2}) = ", good_fibonacci(n)[0])
    print("number of calls: ", num_call_good)
