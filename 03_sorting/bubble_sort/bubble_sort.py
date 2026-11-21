import time
from typing import Callable

def bubble_sort_v1(array: list, inplace: bool = False) -> list:
    """Bubbles the smallest unsorted element to the front on each pass."""
    arr = array if inplace else array.copy()
    if not arr:
        return arr

    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr

def bubble_sort_v2(array: list, inplace: bool = False) -> list:
    """Bubbles the largest unsorted element to the back on each pass."""
    arr = array if inplace else array.copy()
    if not arr:
        return arr

    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def bubble_sort_v3(array: list, inplace: bool = False) -> list:
    """Optimised bubble sort that exits early if a pass does zero swaps."""
    arr = array if inplace else array.copy()
    if not arr:
        return arr

    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1, i, -1):
            if arr[j] < arr[j - 1]:
                swapped = True
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
        if not swapped:
            break

    return arr

def runtime(func: Callable, data: list) -> float:
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    N = 1000
    test_cases = {
        "Already Sorted": list(range(N)),
        "Almost Sorted": list(range(1, N)) + [0],
        "Reverse Sorted": list(range(N - 1, -1, -1))
    }

    print("Runtime comparison across three versions of bubble sort:\n")
    print(f"| {'Input Case':<15} | {'v1 (Left)':<12} | {'v2 (Right)':<12} | {'v3 (Early Exit)':<15} |")
    print(f"|{'-' * 17}|{'-' * 14}|{'-' * 14}|{'-' * 17}|")
    for name, dataset in test_cases.items():
        t1 = runtime(bubble_sort_v1, dataset)
        t2 = runtime(bubble_sort_v2, dataset)
        t3 = runtime(bubble_sort_v3, dataset)

        print(f"| {name:<15} | {t1 * 1000:>10.2f}ms | {t2 * 1000:>10.2f}ms | {t3 * 1000:>13.2f}ms |")