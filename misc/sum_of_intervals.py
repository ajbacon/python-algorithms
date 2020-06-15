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

# relatively inefficient solution, this can probably be improved


# ------------------------------TESTING-------------------------------------
import unittest


class CoinChange(unittest.TestCase):

    def setUp(self):
        pass

    def test_one_interval(self):
        """it should return 3 given one interval of [(1,4)]"""
        intervals = [
            (1, 4)
        ]
        res = sum_of_intervals(intervals)
        self.assertEqual(res, 3)

    def test_two_intervals_no_overlap(self):
        """it should return 6 given two intervals [(1,4), (6,9)]"""
        intervals = [
            (1, 4),
            (6, 9)
        ]
        res = sum_of_intervals(intervals)
        self.assertEqual(res, 6)

    def test_two_intervals_with_overlap(self):
        """it should return 8 given two intervals [(1,4), (3,9)]"""
        intervals = [
            (1, 4),
            (3, 9)
        ]
        res = sum_of_intervals(intervals)
        self.assertEqual(res, 8)

    def test_two_intervals_with_complete_overlap(self):
        """it should return the correct result given complete overlap of second interval"""
        intervals = [
            (1, 10),
            (3, 9)
        ]
        res = sum_of_intervals(intervals)
        self.assertEqual(res, 9)

    def test_three_intervals_mixture_of_overlaps(self):
        """it should return 7 given three unordered intervals [(1,4), (7,10), (3,5)]"""
        intervals = [
            (1, 4),
            (7, 10),
            (3, 5)
        ]
        res = sum_of_intervals(intervals)
        self.assertEqual(res, 7)

    def test_many_intervals_mixture_of_overlaps(self):
        """it should return 19 given many unordered and various overlapping """
        intervals = [
            (1, 5),
            (10, 20),
            (1, 6),
            (16, 19),
            (5, 11)
        ]
        res = sum_of_intervals(intervals)
        self.assertEqual(res, 19)


if __name__ == '__main__':
    unittest.main()


# intervals = [
#     (1, 4)
# ]
# res = sum_of_intervals(intervals)
# print(res, res == 3)


# intervals = [
#     (1, 4),
#     (7, 10),
#     (3, 5)
# ]
# res = sum_of_intervals(intervals)
# print(res, res == 7)

# intervals = [
#     (1, 5),
#     (10, 20),
#     (1, 6),
#     (16, 19),
#     (5, 11)
# ]
# res = sum_of_intervals(intervals)
# print(res, res == 19)
