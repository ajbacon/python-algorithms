# codewars kata: https://www.codewars.com/kata/54eb33e5bc1a25440d000891


# ------------------------initial attempt----------------------------
import math


def square_into_squares(n):
    target_sum = n * n
    return square_into_squares_rec(target_sum, n, [])


def square_into_squares_rec(current_sum, current_square, square_vals):
    if current_sum == 0:
        return True

    if current_sum < 0:
        return False

    if current_square == 0:
        return False

    for i in range(current_square - 1, 0, -1):
        square_vals.append(i)
        current_sum -= i * i
        new_i = 1
        if current_sum > 0:
            new_i = int(math.sqrt(current_sum)) + 1

        if(square_into_squares_rec(current_sum, i, square_vals)):
            return square_vals[::-1]
        square_vals.pop()
        current_sum += i * i

    return False


# ----------------updated attempt----------------------


def decompose(n):
    target = 0
    stack = [n]
    while stack:
        current = stack.pop()

        target += current ** 2
        for i in range(current - 1, 0, -1):
            if target - (i ** 2) >= 0:
                target -= i ** 2
                stack.append(i)
                if target == 0:
                    stack.sort()
                    return stack
    return None


print(square_into_squares(5))

print(decompose(5))

# ------------------------------TESTING-------------------------------------
import unittest


class SquareIntoSquares(unittest.TestCase):

    def setUp(self):
        pass

    # def test_one_interval(self):
    #     """it should return 3 given one interval of [(1,4)]"""
    #     intervals = [
    #         (1, 4)
    #     ]
    #     res = sum_of_intervals(intervals)
    #     self.assertEqual(res, 3)
