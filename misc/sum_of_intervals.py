# codewars kata: https://www.codewars.com/kata/sum-of-intervals/python

def sum_of_intervals(intervals):
    intervals.sort()
    length = len(intervals)
    if length == 1:
        return intervals[0][1] - intervals[0][0]

    start, finish = intervals[0]
    new_arr = [intervals[0]]
    for i in range(1, length):
        new_start, new_finish = intervals[i]
        if new_start <= finish:
            finish = max(finish, new_finish)
            new_arr[-1] = (start, finish)
        else:
            start, finish = intervals[i]
            new_arr.append(intervals[i])

    sum = 0
    for el in new_arr:
        sum += (el[1] - el[0])

    return sum

# Complexity
# ----------
# sort method used, this runs at time O(nlogn)
# then intervals and new_arr looped over once each, both @ O(n)
# Hence, overall complexity O(nlogn)


# new_arr holds output at space O(n)
# hence overall space complexity O(n)


# ------------------------------TESTING-------------------------------------
import unittest


class CoinChange(unittest.TestCase):

    def setUp(self):
        pass

    def test_simple_1_denomination_sum1(self):
        """it should return 1 given denominations of [1] and target of 1"""
        denoms = [1]
        target = 1
        res = change(denoms, len(denoms), target)
        self.assertEqual(res, 1)


intervals = [
    (1, 4)
]
res = sum_of_intervals(intervals)
print(res, res == 3)


intervals = [
    (1, 4),
    (7, 10),
    (3, 5)
]
res = sum_of_intervals(intervals)
print(res, res == 7)

intervals = [
    (1, 5),
    (10, 20),
    (1, 6),
    (16, 19),
    (5, 11)
]
res = sum_of_intervals(intervals)
print(res, res == 19)
