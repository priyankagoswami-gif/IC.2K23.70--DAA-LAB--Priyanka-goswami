
tasks = ["Task1", "Task2", "Task3", "Task4", "Task5"]
# 1. Stack - LIFO
stack = []
for task in tasks:
    stack.append(task)
print("Stack completion order:")
while stack:
    print(stack.pop())
# 2. Queue - FIFO
tas = tasks.copy()
#tasks = ["Task1", "Task2", "Task3", "Task4", "Task5"]
queue = []
for task in tas:
    queue.append(task)
print("Queue completion order:")
while queue:
    print(queue.pop(0))
# 3. Printer - Queue
print("\nPrinter should use: Queue")
print("Printer order:")

for task in tas:
    print(task)