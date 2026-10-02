# Program to perform operations on a 2D array

def display(matrix):
    for row in matrix:
        print(row)


def insert_row(matrix):
    index = int(input("Enter position to insert row: "))

    if index < 0 or index > len(matrix):
        print("Invalid position")
        display(matrix)
        return

    row = []
    for i in range(len(matrix[0])):
        row.append(int(input("Enter element: ")))

    matrix.insert(index, row)

    print("After insertion:")
    display(matrix)


def delete_row(matrix):
    index = int(input("Enter position to delete row: "))

    if index < 0 or index >= len(matrix):
        print("Invalid position")
        display(matrix)
        return

    matrix.pop(index)

    print("After deletion:")
    display(matrix)


def search(matrix):
    value = int(input("Enter value to search: "))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == value:
                print("Value found at row", i, "column", j)
                display(matrix)
                return

    print("Value not found")
    display(matrix)


def rotate(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = []

    for j in range(cols):
        row = []

        for i in range(rows - 1, -1, -1):
            row.append(matrix[i][j])

        result.append(row)

    matrix[:] = result

    print("After 90 degree clockwise rotation:")
    display(matrix)


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input("Enter element: ")))
    matrix.append(row)

print("Original array:")
display(matrix)

insert_row(matrix)
delete_row(matrix)
search(matrix)
rotate(matrix)
