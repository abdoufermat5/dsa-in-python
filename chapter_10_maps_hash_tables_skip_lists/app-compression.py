def div_method(hash_code, N):
    return hash_code % N


def mad_method(hash_code, N, a, b, p):
    return ((hash_code * a + b) % p) % N


if __name__ == '__main__':
    test_hash = [101, 202, 303]
    N = 101
    a = 3
    b = 3
    p = 5

    print("Testing Division method:")
    for h in test_hash:
        print("compression of ", h, "is: ", div_method(h, N))

    print("Testing MAD method:")
    for h in test_hash:
        print("compression of ", h, "is: ", mad_method(h, N, a, b, p))
