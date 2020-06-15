import unittest


def num_subsets(arr, m, sum):

    if arr == []:
        return 0

    # Base cases
    if sum == 0:
        return 1  # if sum is zero we have a solution, therefore +1

    if sum < 0:
        return 0  # if sum goes below 0 we have gone too far, hence not a solution

    if m == 0:
        return 0  # reached the end of the array and implicitly the sum isn't <= 0

    # return a recursive function summing count when the solution
    # a) uses arr[m - 1]
    # b) does not use arr[m - 1], hence removes from the count call
    return num_subsets(arr, m - 1, sum) + num_subsets(arr, m - 1, sum - arr[m - 1])


class MergeSort(unittest.TestCase):

    def setUp(self):
        pass

    def test_empty_array(self):
        """it should return 0 for an empty array"""
        res = num_subsets([], 0, 0)
        self.assertEqual(res, 0)

    def test_simple_1_element_arr(self):
        """it should return 1 when target sum is the only number in the array"""
        res = num_subsets([1], 1, 1)
        self.assertEqual(res, 1)

    def test_4_element_arr_with_multiple_solutions(self):
        """it should return the correct answer when there are multiple solutions"""
        res = num_subsets([2, 4, 6, 10], 4, 6)
        self.assertEqual(res, 2)

    def test_5_element_arr_with_multiple_solutions(self):
        """it should return the correct answer when there are multiple solutions"""
        res = num_subsets([1, 2, 3, 6, 9], 5, 9)
        self.assertEqual(res, 3)

    def test_multi_element_arr_with_no_solutions(self):
        """it should return the correct answer when there are multiple solutions"""
        res = num_subsets([5, 6, 7], 3, 10)
        self.assertEqual(res, 0)


if __name__ == '__main__':
    unittest.main()
