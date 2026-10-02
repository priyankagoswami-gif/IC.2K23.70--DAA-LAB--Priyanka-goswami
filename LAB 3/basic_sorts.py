# Bubble Sort, Selection Sort and Insertion Sort
def bubble_sort(arr):
    a = arr.copy()

    print("\nBubble Sort")
    print("Original:", a)

    for i in range(len(a) - 1):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

        print("step", i + 1, ":", a)

    return a


def selection_sort(arr):
    a = arr.copy()

    print("\nSelection Sort")
    print("Original:", a)

    for i in range(len(a) - 1):
        m = i

        for j in range(i + 1, len(a)):
            if a[j] < a[m]:
                m = j

        a[i], a[m] = a[m], a[i]

        print("Step", i + 1, ":", a)

    return a


def insertion_sort(arr):
    a = arr.copy()

    print("\nInsertion Sort")
    print("Original:", a)

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j = j - 1

        a[j + 1] = key

        print("Step", i, ":", a)

    return a


# Main program

arr = [5, 2, 8, 1, 9]

bubble_sort(arr)
selection_sort(arr)
insertion_sort(arr)
