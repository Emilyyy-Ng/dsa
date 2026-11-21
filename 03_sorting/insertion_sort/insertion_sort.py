import time
from typing import Callable

def insertion_sort_v1(array: list, inplace: bool = False) -> list:
    """Insert arr[i] into arr[0...i-1] so that arr[0...i] is sorted on each pass i."""
    arr = array if inplace else array.copy()
    if not arr:
        return arr

    n = len(arr)
    for i in range(n):
        j = i
        while j > 0:
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr

def insertion_sort_v2(array: list, inplace: bool = False) -> list:
    """Optimised insertion sort that exits the inner loop early
    if arr[0...i] is already sorted"""
    arr = array if inplace else array.copy()
    if not arr:
        return arr

    n = len(arr)
    for i in range(n):
        j = i
        while j > 0:
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1
            else: # early exit if arr[0...i] is already sorted
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

    print("Runtime comparison across two versions of insertion sort:\n")
    print(f"| {'Input Case':<15} | {'v1':<12} | {'v2 (Early Exit)':<15} |")
    print(f"|{"-" * 17}|{"-" * 14}|{"-" * 17}|")
    for name, dataset in test_cases.items():
        t1 = runtime(insertion_sort_v1, dataset)
        t2 = runtime(insertion_sort_v2, dataset)

        print(f"| {name:<15} | {t1 * 1000:>10.2f}ms | {t2 * 1000:>13.2f}ms |")