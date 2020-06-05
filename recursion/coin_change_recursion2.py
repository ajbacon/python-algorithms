def count(S, m, n):

    # Base cases:
    if (n == 0):  # if n is 0 then a solution is found, hence return 1
        return 1

    if (n < 0):  # if n < 0 then we have overshoot the target and no solution exists
        return 0

    if (m <= 0):  # if there are no coins and n is implicitly above 0 (because of above if statement)
        return 0

    # return a recursive function summing count when
    # a) the solution uses S[m - 1]
    # b) does not use S[m - 1], hence removes from the count call

    return count(S, m, n - S[m - 1]) + count(S, m - 1, n)


arr = [1, 2, 3]
m = len(arr)
print(count(arr, m, 5))
