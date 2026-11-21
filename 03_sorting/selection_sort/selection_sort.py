def selection_sort(array: list, inplace: bool = False) -> list:
    """Sorts an array by repeatedly selecting the minimum element."""
    arr = array if inplace else array.copy()
    if not arr:
        return arr

    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == "__main__":
    arr = list(range(10, 0, -1))
    print("Original:", arr)
    print("Sorted:", selection_sort(arr))