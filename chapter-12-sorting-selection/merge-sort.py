def merge(s1, s2, s):
    i = j = 0
    while i + j < len(s):
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            s[i + j] = s1[i]
            i += 1
        else:
            s[i + j] = s2[j]
            j += 1


def merge_sort(s):

    n = len(s)
    if n < 2:
        return

    m = n//2
    s1 = s[0:m]
    s2 = s[m:n]
    merge_sort(s1)
    merge_sort(s2)

    merge(s1, s2, s)


if __name__ == "__main__":
    arr = [100, 1, 5, 2, 3, 6, 4, -1]
    merge_sort(arr)
    print(arr)