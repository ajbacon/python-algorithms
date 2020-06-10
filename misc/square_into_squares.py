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


# def test(num):
#     x = int(math.sqrt(num))
#     print(x)


# test(17)
