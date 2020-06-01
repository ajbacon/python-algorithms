
def zipper():
    fruits = ['apples', 'oranges', 'bananas']
    quantities = [5, 3, 4]
    prices = [1.50, 2.25, 0.89]

    i = 0
    output = []
    for fruit in fruits:
        for qty in quantities:
            for price in prices:
                output.append((fruit, qty, price))
        i += 1
    return output


print(zipper())
