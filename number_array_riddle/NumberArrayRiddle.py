"""
Problem: Given an unordered array of integers from 1-100, if we remove 2 random
integers from the list, how do you find which 2 integers were removed?
Solution ideally only uses 1 loop
"""

from cmath import sqrt
import random


def find2Missing(iList: "list[int]") -> "list[int]":
    completeList = list(range(1, 101))
    completeProduct = 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
    completeSum = 5050
    # this for loop has been hardcoded
    # for i in completeList:
    #     completeProduct *= i
    #     completeSum += i

    incompleteProduct = 1
    incompleteSum = 0
    for i in iList:
        incompleteProduct *= i
        incompleteSum += i

    missingProduct = completeProduct/incompleteProduct
    missingSum = completeSum - incompleteSum

    answer = findNosFromSumAndProd(missingSum, missingProduct)

    return answer


def findNosFromSumAndProd(sum: int, prod: int) -> "list[int]":
    # sum = x + y
    # prod = x * y
    # x = sum - y
    # prod = (sum - y) * y
    # prod = sum * y - y^2
    # y^2 - sum * y + prod = 0
    # ~~~
    # https://math.stackexchange.com/questions/171407/finding-two-numbers-given-their-sum-and-their-product
    # x and y roots will just mirror each other
    # So can just find one set to get answer
    y = findRoots(1, -sum, prod)
    return y


def findRoots(a, b, c):
    # Find roots using quadratic formula
    # following ax^2 + bx + c = 0
    # https://www.geeksforgeeks.org/print-a-pair-of-numbers-with-the-given-sum-and-product/
    # ~~~
    # This function assumes equation WILL have a root,
    # and that roots will not be the same
    d = b**2 - 4 * a * c
    sqrtVal = sqrt(abs(d))
    if d > 0:
        x = -b + sqrtVal
        y = -b - sqrtVal
        root1 = x / 2 * a
        root2 = y / 2 * a
        return [root1, root2]
    return


incompleteList = list(range(1, 101))

# Pop 2 random integers
randIntIndex1 = random.randint(0, 99)
# 98 because 1 number would've been removed
randIntIndex2 = random.randint(0, 98)
randInt1 = incompleteList.pop(randIntIndex1)
randInt2 = incompleteList.pop(randIntIndex2)
print("Removed Numbers: ", randInt1, randInt2)
print("Found answers  : ", find2Missing(incompleteList))
