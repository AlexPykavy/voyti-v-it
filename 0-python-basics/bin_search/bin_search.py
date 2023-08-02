def bin_search(list, x):
    low = 0
    high = len(list) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        if list[mid] < x:
            low = mid + 1

        elif list[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1


if __name__ == "__main__":
    list = [2, 3, 4, 10, 40]
    x = 10

    result = bin_search(list, x)

    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("None")
