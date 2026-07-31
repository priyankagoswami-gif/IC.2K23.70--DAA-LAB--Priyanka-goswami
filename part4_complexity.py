
# Single Loop
print("Single loop for i = 1 to 5:")
count = 0
for i in range(1, 6):
    print(i)
    count += 1
print("Number of runs:", count)
# Nested Loop
print("\nNested loop for i = 1 to 5 and j = 1 to 5:")
count = 0
for i in range(1, 6):
    for j in range(1, 6):
        print(i, j)
        count += 1
print("Total PRINT runs:", count)
# For n = 20
n = 20
single_loop = n
nested_loop = n * n
print("\nFor n = 20:")
print("Single loop runs:", single_loop)
print("Nested loop PRINT runs:", nested_loop)
# For n = 10
n = 10
single_loop = n
nested_loop = n * n
print("\nFor n = 10:")
print("Single loop runs:", single_loop)
print("Nested loop PRINT runs:", nested_loop)