def quicksort(arr, left, right):

    if len(arr) > 1:
        index = get_pivot(arr, left, right)
        print(index)
        # sort left of pivot
        if left < index:
            quicksort(arr, left, index - 1)
        # sort right of pivot
        if index < right:
            quicksort(arr, index, right)

    return arr


def get_pivot(arr, left, right):
    i = left
    j = right
    pivot = arr[(left + right) // (right - left + 1)]
    while i <= j:
        while arr[i] < pivot:
            i += 1

        while arr[j] > pivot:
            j -= 1

        if i <= j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1

    return i


res = quicksort([2], 0, 0)
print(res, res == [2])
res = quicksort([3, 2, 1], 0, 1)
print(res, res == [1, 2])
