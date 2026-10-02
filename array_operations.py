# Program to perform operations on a 1D array

def insert(arr):
    index = int(input("Enter index to insert: "))
    value = int(input("Enter value: "))

    if index <  index > len(arr):
        print("Invalid index")
        print("Array:", arr)
        return

    arr.insert(index, value)
    print("After insertion:", arr)


def delete(arr):
    index = int(input("Enter index to delete: "))

    if index < 0 or index >= len(arr):
        print("Invalid index")
        print("Array:", arr)
        return

    arr.pop(index)
    print("After deletion:", arr)


def search(arr):
    value = int(input("Enter value to search: "))

    for i in range(len(arr)):
        if arr[i] == value:
            print("Value found at index", i)
            print("Array:", arr)
            return

    print("Value not found")
    print("Array:", arr)


def left_rotate(arr):
    k = int(input("Enter k for left rotation: "))

    if len(arr) == 0:
        print("Array is empty")
        return

    k = k % len(arr)
    arr[:] = arr[k:] + arr[:k]

    print("After left rotation:", arr)


def right_rotate(arr):
    k = int(input("Enter k for right rotation: "))

    if len(arr) == 0:
        print("Array is empty")
        return

    k = k % len(arr)
    arr[:] = arr[-k:] + arr[:-k] if k != 0 else arr

    print("After right rotation:", arr)


n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

print("Original array:", arr)

insert(arr)
delete(arr)
search(arr)
left_rotate(arr)
right_rotate(arr)