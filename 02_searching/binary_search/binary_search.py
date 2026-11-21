import bisect

def binary_search_iterative(arr: list[int], target: int) -> int:
    """Return the index of the target, or -1 if not found. Input array must be sorted."""
    low = 0
    up = len(arr) - 1

    while low <= up:
        mid = (low + up) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            up = mid - 1
    return -1

def binary_search_recursive(arr: list[int], target: int, low: int = 0, up: int | None = None) -> int:
    """Return the index of the target, or -1 if not found. Input array must be sorted."""
    if up is None:
        up = len(arr) - 1

    if low > up:
        return -1

    mid = (low + up) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, up)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

if __name__ == "__main__":
    arr = [i for i in range(10)]
    print(f"array: {arr}")

    target = 2
    print(f"\nSearching for {target}...")

    # ----- Custom Binary Search -----
    print(f"Iterative result: {binary_search_iterative(arr, target)}")
    print(f"Recursive result: {binary_search_recursive(arr, target)}")

    # ----- Python's Standard Library -----
    print(f"Bisect result: {bisect.bisect_left(arr, target)}")