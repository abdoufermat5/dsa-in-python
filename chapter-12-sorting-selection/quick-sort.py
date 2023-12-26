import random

m = {0: 0, 1: 0, 2: 0}


def quicksort(arr):
    global m
    m[0] += 1
    if len(arr) <= 1:
        return arr
    p = arr[0]
    left = [i for i in arr[1:] if i <= p]
    right = [i for i in arr[1:] if i > p]

    return quicksort(left) + [p] + quicksort(right)


def randomized_partition(arr, low, high):
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]
    return partition(arr, low, high)


def partition(arr, l, r):
    p = arr[r]
    i = l - 1
    # i is the last index of all elements that are less than p
    # we use j to go through elements and update the value of i
    for j in range(l, r):
        if arr[j] <= p:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def quicksort_inplace(arr, l, r):
    global m
    m[1] += 1
    if l < r:
        p = partition(arr, l, r)
        quicksort_inplace(arr, l, p - 1)
        quicksort_inplace(arr, p + 1, r)


def quicksort_inplace_2(arr, l, r):
    global m
    m[2] += 1
    if l >= r:
        return
    p = arr[r]
    a = l
    b = r - 1
    while a <= b:
        while a <= b and arr[a] <= p:
            a += 1
        while a <= b and arr[b] >= p:
            b -= 1
        if a <= b:
            arr[a], arr[b] = arr[b], arr[a]
            a += 1
            b -= 1

    arr[a], arr[r] = arr[r], arr[a]

    quicksort_inplace_2(arr, l, a - 1)
    quicksort_inplace(arr, a + 1, r)


if __name__ == "__main__":
    arr = [100, 1, 5, 2, 3, 6, 4, -1]
    quicksort(arr)

    arr = [100, 1, 5, 2, 3, 6, 4, -1]
    quicksort_inplace(arr, 0, 7)

    arr = [100, 1, 5, 2, 3, 6, 4, -1]
    quicksort_inplace_2(arr, 0, 7)

    print(m)
