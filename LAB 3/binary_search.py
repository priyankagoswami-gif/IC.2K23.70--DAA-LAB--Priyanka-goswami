# Binary Search

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# Main program

arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]

print("Array:", arr)

target = 23
result = binary_search(arr, target)

if result != -1:
    print("23 found at index:", result)
else:
    print("23 not found")
