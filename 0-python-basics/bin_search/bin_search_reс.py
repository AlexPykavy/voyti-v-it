def bin_search_rec(list, low, high, x):

    if high >= low:

        mid = (high + low) // 2

        if list[mid] == x:
            return mid

        elif list[mid] > x:
            return bin_search_rec(list, low, mid - 1, x)

        else:
            return bin_search_rec(list, mid + 1, high, x)

    else:

        return -1


if __name__ == "__main__":
    list = [2, 3, 4, 10, 40]
    x = 10
    result = bin_search_rec(list, x)

    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("None")
