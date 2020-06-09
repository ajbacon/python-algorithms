def merge_sort(A):
    merge_sort_rec(A, 0, len(A) - 1)

    return A


def merge_sort_rec(A, first, last):
    if first < last:
        middle = (first + last) // 2
        merge_sort_rec(A, first, middle)
        merge_sort_rec(A, middle + 1, last)
        merge(A, first, middle, last)


def merge(A, first, middle, last):
    L = A[first:middle + 1]
    R = A[middle + 1:last + 1]
    # L.append(9999999999)
    # R.append(9999999999)

    i = 0
    j = 0

    for k in range(first, last + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


# print(merge([3, 4, 1, 2], 0, 1, 3))

print(merge_sort([4, 3, 2, 1]))
