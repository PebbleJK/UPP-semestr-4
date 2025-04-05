def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i  # Zakładamy, że aktualny indeks to minimum

        # Szukamy najmniejszego elementu w pozostałej części
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Zamieniamy znalezione minimum z aktualnym elementem
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [64, 25, 12, 22, 11]
print("Przed sortowaniem:", arr)
selection_sort(arr)
print("Po sortowaniu:    ", arr)
