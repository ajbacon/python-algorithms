
# Given value 'n' and array of coin denominations 'S'
# How many unique permutations of change can be made from given denominations
# assume infinite amount of each denomination
# m is the length of the array

def change(S, m, n):

    # Base cases:
    if (n == 0):  # if n is 0 then a solution is found, hence return 1
        return 1

    if (n < 0):  # if n < 0 then we have overshot the target and no solution exists
        return 0

    if (m <= 0):  # if there are no coins and n is implicitly above 0 (because of above if statement)
        return 0

    # return a recursive function summing count when
    # a) the solution uses S[m - 1]
    # b) does not use S[m - 1], hence removes from the count call

    return change(S, m, n - S[m - 1]) + change(S, m - 1, n)


# ------------------------------TESTING-------------------------------------
import unittest


class MergeSort(unittest.TestCase):

    def setUp(self):
        pass

    def test_simple_1_denomination_sum1(self):
        """it should return 1 given denominations of [1] and target of 1"""
        denoms = [1]
        target = 1
        res = change(denoms, len(denoms), target)
        self.assertEqual(res, 1)

    def test_3_denominations_sum4(self):
        """it should return 1 given denominations of [1] and target of 1"""
        denoms = [1, 2, 3]
        target = 4
        res = change(denoms, len(denoms), target)
        self.assertEqual(res, 4)

    def test_4_denominations_sum10(self):
        """it should return 1 given denominations of [2, 5, 3, 6] and target of 10"""
        denoms = [2, 5, 3, 6]
        target = 10
        res = change(denoms, len(denoms), target)
        self.assertEqual(res, 5)

    def test_no_solution(self):
        """it should return 0 given denominations of [1] and target of 1"""
        denoms = [2, 4, 6]
        target = 11
        res = change(denoms, len(denoms), target)
        self.assertEqual(res, 0)


if __name__ == '__main__':
    unittest.main()
