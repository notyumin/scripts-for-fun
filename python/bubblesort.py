import time
from collections.abc import Callable

def bubble_sort_v1(num_list: list[int]):
    # for every number, compare itself to all numbers behind, and swap accordingly
    for i in range(len(num_list)-1):
        for j in range(i+1, len(num_list)):
            print(f'Comparing {num_list[i]} > {num_list[j]}')
            if num_list[i] > num_list[j]:
                print("List before swap:", num_list)
                # swap
                temp = num_list[i]
                num_list[i] = num_list[j]
                num_list[j] = temp
                print("List after swap:", num_list)
            print()
    return num_list

def bubble_sort_v2(num_list: list[int]):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(num_list)-1):
            print(f"Comparing {num_list[i]} to {num_list[i+1]}")
            if num_list[i] > num_list[i+1]:
                # swap
                print("Preswap:", num_list)
                temp = num_list[i]
                num_list[i] = num_list[i + 1]
                num_list[i + 1] = temp
                swapped = True
                print("Postswap:", num_list)
    return num_list

def bubbble_sort_v3(num_list: list[int]):
    return num_list

def time_sort(sort_fn: Callable[[list[int]], list[int]]):
    start = time.time()
    initial_list = [78,8,5,2,9,1,24]
    sort_fn(initial_list)
    end = time.time()
    return end - start

v1 = time_sort(bubble_sort_v1)
v2 = time_sort(bubble_sort_v2)

print("v1:", v1)
print("v2:", v2)
