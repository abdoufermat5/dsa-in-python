def reverse(arr, start, end):
    if start < end - 1:
        arr[start], arr[end-1] = arr[end-1], arr[start]
        reverse(arr, start+1, end-1)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 0, -1, 10]
    print("original arr", arr)
    reverse(arr, 0, 7)
    print("reversed arr", arr)