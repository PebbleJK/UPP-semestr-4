import random

def insertion_sort(arr):
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        comparisons += 1 if j >= 0 else 0  # Porównanie, gdy warunek while nie jest spełniony
        arr[j + 1] = key
    return comparisons

def merge(left, right):
    merged = []
    comparisons = 0
    i = j = 0
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, comparisons

def merge_sort(arr, run_size):
    if len(arr) <= run_size:
        comparisons = insertion_sort(arr)
        return arr, comparisons
    
    mid = len(arr) // 2
    left, left_comparisons = merge_sort(arr[:mid], run_size)
    right, right_comparisons = merge_sort(arr[mid:], run_size)
    merged, merge_comparisons = merge(left, right)
    total_comparisons = left_comparisons + right_comparisons + merge_comparisons
    return merged, total_comparisons

def generate_arrays(size):
    sorted_array = list(range(1, size + 1))
    partially_sorted_array = sorted_array[:size // 2] + random.sample(range(size // 2, size + 1), size // 2)
    random_array = random.sample(range(1, size + 1), size)
    reversed_array = sorted_array[::-1]
    return sorted_array, partially_sorted_array, random_array, reversed_array

def test_algorithms():
    size = 30
    run_sizes = [5, 10, 15]
    arrays = generate_arrays(size)
    array_types = ['Posortowana', 'Częściowo posortowana', 'Losowa', 'Odwrócona']
    
    for run_size in run_sizes:
        print(f"\nRozmiar run: {run_size}")
        for arr_type, arr in zip(array_types, arrays):
            test_array = arr[:]
            _, comparisons = merge_sort(test_array, run_size)
            print(f"{arr_type}: Liczba porównań = {comparisons}")

test_algorithms()
