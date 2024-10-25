"""
Possible solution:
1. Get the first number, and check what the other numbers need to result in
to get the result
e.g. For 100, to get 364, you need 264

2. Recurse through rest of numbers to see if each result can be achieved
e.g. With 25, is it possible to get 264

3. Make sure to test for all operations (+, -, *, /)

4. Also make sure to test every single order of numbers
e.g. [a, b, c]
a + b + c
a - b - c
a + b - c
a - b + c
a + b * c
a + b / c
etc...
"""

target: int = 952
numbers: 'list[int]' = [25, 50, 75, 100, 3, 6]


def printAnswer(numbers: 'list[int]', number: int, operation: str, target: int):
    if len(numbers) == 1:
        print(numbers[0], operation, number, "=", target)
    else:
        print(operation, number, "=", target)


def checkCanBeDone(numbers: 'list[int]', target: int) -> bool:

    # base condition
    if len(numbers) <= 1:
        first, *rest = numbers
        return first == target

    for i in range(len(numbers)):
        numbersCopy = numbers.copy()  # Make a copy to avoid mutation
        number = numbersCopy.pop(i)

        # Check for +
        if checkCanBeDone(numbersCopy, target - number):
            printAnswer(numbersCopy, number, "+", target)
            return True

        # Check for -
        if checkCanBeDone(numbersCopy, target + number):
            printAnswer(numbersCopy, number, "-", target)
            return True

        # Check for *
        if checkCanBeDone(numbersCopy, target / number):
            printAnswer(numbersCopy, number, "*", target)
            return True

        # Check for /
        if checkCanBeDone(numbersCopy, target * number):
            printAnswer(numbersCopy, number, "/", target)
            return True

    return False


if checkCanBeDone(numbers, target) == False:
    print("There is no solution")
