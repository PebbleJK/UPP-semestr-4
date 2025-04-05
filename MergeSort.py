def merge_sort(arr):
    if len(arr) > 1:
        # Dzielenie tablicy na dwie części
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Rekurencyjne sortowanie obu połówek
        merge_sort(left_half)
        merge_sort(right_half)

        # Scalanie posortowanych połówek
        i = j = k = 0

        # Łączenie elementów z left_half i right_half do arr
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Dodanie pozostałych elementów z left_half (jeśli są)
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Dodanie pozostałych elementów z right_half (jeśli są)
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


arr = [38, 27, 43, 3, 9, 82, 10]
print("Przed sortowaniem:", arr)
merge_sort(arr)
print("Po sortowaniu:    ", arr)
