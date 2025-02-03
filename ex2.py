def filter_par(arr: list) -> list:
    x = list(filter(lambda x: x % 2 == 0, arr))

    return x

print(filter_par([1, 2, 3, 4, 5, 6, 8, 10]))