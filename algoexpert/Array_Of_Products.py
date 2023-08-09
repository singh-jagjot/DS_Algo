from typing import List


def array_of_products(array: List):
    products = [1 for _ in range(len(array))]
    left_product = right_product = 1
    for i in range(len(array)):
        products[i] = left_product
        left_product *= array[i]

    for i in reversed(range(len(array))):
        products[i] *= right_product
        right_product *= array[i]

    return products


print(array_of_products([5, 1, 4, 2]))
