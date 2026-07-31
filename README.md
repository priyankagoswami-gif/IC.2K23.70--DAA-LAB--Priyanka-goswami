Lab Task 

Part 1. Trace It Yourself

Input:
"[8, 3, 15, 6, 2]"

Output:
Largest number: "15"
Total comparisons: "4"

Comparisons made: "4"

Dry Run:

- i = 1, A[i] = 3, max = 8, comparisons = 1
- i = 2, A[i] = 15, max = 15, comparisons = 2
- i = 3, A[i] = 6, max = 15, comparisons = 3
- i = 4, A[i] = 2, max = 15, comparisons = 4

Sorting method used: Bubble Sort

Sorting steps:

- After Pass 1: "[3, 8, 6, 2, 15]"
- After Pass 2: "[3, 6, 2, 8, 15]"
- After Pass 3: "[3, 2, 6, 8, 15]"
- After Pass 4: "[2, 3, 6, 8, 15]"

Final sorted list: "[2, 3, 6, 8, 15]"

Explanation:

The code checks every element once to find the largest number. It compares each element with "maxi" and updates "maxi" if a larger value is found.

---

Part 2. Stack or Queue

Stack order:
"Task5 → Task4 → Task3 → Task2 → Task1"

Queue order:
"Task1 → Task2 → Task3 → Task4 → Task5"

Printer should use: Queue

Reason:
A printer should process tasks in the order they arrive. Queue follows FIFO (First In, First Out).

Dry Run:

Stack (LIFO):
Push "Task1, Task2, Task3, Task4, Task5" and then pop in reverse order.

Queue (FIFO):
Enqueue "Task1" to "Task5" and then dequeue them in the same order.

Explanation:

A printer needs first-come-first-served order so that the task received first is completed first. A Queue guarantees this order using the FIFO principle.

---

Part 4. Count the Steps

Single loop runs: "5"

Nested loop total prints: "25"

Dry Run:

Single loop:
"i = 1 to 5" → prints "5" times.

Nested loop:
"i = 1 to 5" and "j = 1 to 5" → inner print runs "5" times for each "i".

Total:

"5 × 5 = 25"

For n = 20:

Single loop runs: "20"

Nested loop runs: "400"

For n = 10:

Single loop runs: "10"

Nested loop runs: "100"

Explanation:

The single loop grows linearly because it runs "n" times, giving O(n) complexity. The nested loop runs "n × n" times, giving O(n²) complexity.
