# NOT COMPLETE

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


class QuickSort(unittest.TestCase):

    def setUp(self):
        pass

    def test_one_element_input(self):
        """it should return the same arr when only one element is input"""
        res = merge_sort([1])
        self.assertEqual(res, [1])

    def test_two_element_input(self):
        """it should sort an array of 2 elements"""
        res = merge_sort([2, 1])
        self.assertEqual(res, [1, 2])

    def test_three_element_input(self):
        """it should sort an array of 3 elements"""
        res = merge_sort([2, 1, 3])
        self.assertEqual(res, [1, 2, 3])

    def test_20el_shuffled_array(self):
        """it should sort an array of 20 elements"""
        res = merge_sort([2, 11, 17, 16, 14, 19, 15, 9, 12,
                          5, 1, 18, 4, 20, 7, 3, 8, 10, 13, 6])
        self.assertEqual(res, [1, 2, 3, 4, 5, 6, 7, 8, 9,
                               10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

    def test_20el_sorted_array(self):
        """it should return the correct array for an already shuffled array"""
        res = merge_sort([1, 2, 3, 4, 5, 6, 7, 8, 9,
                          10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        self.assertEqual(res, [1, 2, 3, 4, 5, 6, 7, 8, 9,
                               10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])


if __name__ == '__main__':
    unittest.main()
