def binary_Search(arr, l, r, key):
    if l > r:
        return key, "not found!"
    m = (r + l) // 2
    if arr[m] == key:
        return key, "founded at index ", m
    if arr[m] < key:
        return binary_Search(arr, m+1, r, key)
    else:
        return binary_Search(arr, l, m-1, key)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    key = 5
    print(binary_Search(arr, 0, len(arr)-1, key))