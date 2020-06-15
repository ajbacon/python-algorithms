import unittest


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
    i_max = len(L)
    j_max = len(R)

    for k in range(first, last + 1):
        if i == i_max:
            A[k] = R[j]
            j += 1
        elif j == j_max:
            A[k] = L[i]
            i += 1
        elif (L[i] <= R[j]):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


class MergeSort(unittest.TestCase):

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
        """it should sort an array of 3 elements"""
        res = merge_sort([2, 11, 17, 16, 14, 19, 15, 9, 12,
                          5, 1, 18, 4, 20, 7, 3, 8, 10, 13, 6])
        self.assertEqual(res, [1, 2, 3, 4, 5, 6, 7, 8, 9,
                               10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])


if __name__ == '__main__':
    unittest.main()
