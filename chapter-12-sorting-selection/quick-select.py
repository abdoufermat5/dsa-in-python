import random


def quick_select(arr, k):
    if k < 1:
        print("k must be greater than 0")
        return None
    if len(arr) == 1:
        return arr[0]
    pivot = random.choice(arr)
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    if len(left) == k - 1:  # base case for the recursion
        return pivot
    elif len(left) >= k:
        return quick_select(left, k)
    else:
        # we compute k - len(left) - 1 because we have already removed the pivot and the elements in left
        # so we need to find the k - len(left) - 1 smallest element in right which corresponds to the k smallest
        # element in the original array
        return quick_select(right, k - len(left) - 1)


if __name__ == "__main__":
    arr = [100, 1, 5, 2, 3, 6, 4, -1]
    print(quick_select(arr, 1))
