def num_subsets(arr, m, sum):

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


print(num_subsets([2, 4, 6, 10], 4, 6))
