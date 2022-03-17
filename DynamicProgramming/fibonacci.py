import time


# Recursive Version
def recurs_fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return recurs_fibo(n-1) + recurs_fibo(n-2)


# Dynamic Version
calculated = {}


def d_fibo(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1

    elif n in calculated:
        return calculated[n]

    else:
        calculated[n] = d_fibo(n-1) + d_fibo(n-2)
        return calculated[n]


target = 40

rTimeStart = time.perf_counter()
print(recurs_fibo(target))
rTimeEnd = time.perf_counter()

dTimeStart = time.perf_counter()
print(d_fibo(target))
dTimeEnd = time.perf_counter()

print("Recursive Time:", rTimeEnd - rTimeStart, "seconds")
print("Dynamic Programming Time:", dTimeEnd - dTimeStart, "seconds")
