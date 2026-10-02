# Program 1: 1D Array Operations

### File Name

`array_operations.py`

### Aim

To perform basic operations on a 1D array using Python list, such as insertion, deletion, linear search and left/right rotation.

### Logic

The program takes the array elements from the user. Functions are used for insertion, deletion, searching and rotation. Index values are checked before performing insertion or deletion.

### Operations Performed

* Insert an element at a given index
* Delete an element from a given index
* Search an element using linear search
* Rotate the array to the left
* Rotate the array to the right
* Display the current array

### Sample Input / Output

Sample array:

```text
[10, 20, 30, 40, 50]
```

Insert 25 at index 2:

```text
After insertion: [10, 20, 25, 30, 40, 50]
```

Delete element at index 0:

```text
After deletion: [20, 25, 30, 40, 50]
```

Search for 30:

```text
Value found at index 2
Array: [20, 25, 30, 40, 50]
```

Left rotation by 2:

```text
After left rotation: [40, 50, 20, 25, 30]
```

Right rotation by 2:

```text
After right rotation: [25, 30, 40, 50, 20]
```

### Boundary Case

If an invalid index is entered:

```text
Enter index to insert: 10
Invalid index
Array: [20, 25, 30, 40, 50]
```

---

# Program 2: 2D Array Operations

### File Name

`array_2d_operations.py`

### Aim

To perform insertion, deletion, searching and 90-degree clockwise rotation on a 2D array using Python list of lists.

### Logic

The program stores the matrix using a list of lists. Functions are used for inserting and deleting rows, searching for a value and rotating the complete matrix. The row position is checked before performing insertion or deletion.

### Operations Performed

* Insert a new row at a given position
* Delete a row at a given position
* Search for a value in the entire 2D array
* Rotate the entire array by 90 degrees clockwise
* Display the array row-by-row

### Sample Input / Output

Sample matrix:

```text
[1, 2, 3]
[4, 5, 6]
```

Insert a new row at position 1:

```text
[1, 2, 3]
[7, 8, 9]
[4, 5, 6]
```

Delete row at position 1:

```text
[1, 2, 3]
[4, 5, 6]
```

Search for 5:

```text
Value found at row 1 column 1
[1, 2, 3]
[4, 5, 6]
```

After 90-degree clockwise rotation:

```text
[4, 1]
[5, 2]
[6, 3]
```

### Boundary Case

If an invalid row position is entered:

```text
Enter position to delete row: 10
Invalid position
[1, 2, 3]
[4, 5, 6]
```

