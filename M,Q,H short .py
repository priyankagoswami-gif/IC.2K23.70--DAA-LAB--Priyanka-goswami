# Merge Sort, Quick Sort and Heap Sort


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def quick_sort(arr):
    

    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    smaller = []
    greater = []

    for x in arr[:-1]:
        if x <= pivot:
            smaller.append(x)
        else:
            greater.append(x)

    return quick_sort(smaller) + [pivot] + quick_sort(greater)


def heap(arr, n, i):
    largest = i

    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heap(arr, n, largest)


def heap_sort(arr):
    a = arr.copy()
    n = len(a)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heap(a, n, i)

    # Move largest element to the end
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heap(a, i, 0)

    return a


# Main program

arr = [5, 2, 8, 1, 9]

print("Original Array:", arr)

print("\nMerge Sort:")
print(merge_sort(arr))

print("\nQuick Sort:")
print(quick_sort(arr))

print("\nHeap Sort:")
print(heap_sort(arr))