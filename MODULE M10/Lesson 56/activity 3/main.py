def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

marks = [85, 42, 67, 91, 33, 78]
print("Original:", marks)
print("Sorted:", bubble_sort(marks))
print("Bubble sort is O(n^2) - nested loops over the same input.")
