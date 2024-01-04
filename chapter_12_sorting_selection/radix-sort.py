def counting_sort(arr, expr):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // expr
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // expr
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    neg = [i for i in arr if i < 0]
    pos = [i for i in arr if i >= 0]
    if len(neg) != 0:
        dn = abs(min(neg))
        exp = 1
        while dn // exp > 0:
            counting_sort(neg, exp)
            exp *= 10
    if len(pos) != 0:
        exp = 1
        dp = max(pos)
        while dp // exp > 0:
            counting_sort(pos, exp)
            exp *= 10

    arr[:] = neg + pos


if __name__ == "__main__":
    arr = [-5, 100, 1, 5, 2, 3, 6, 4, -6, -52, -1, -6, 0]
    radix_sort(arr)
    print(arr)
