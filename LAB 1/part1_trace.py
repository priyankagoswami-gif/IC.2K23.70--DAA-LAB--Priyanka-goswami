num = [8,3,15,6,2]
maxi = num[0]
comp = 0
print ("list", num)
for i in range(1, len(num)):
    comp+= 1
    if num[i]>maxi :
        maxi = num[i]
    print("Step", comp, "Current =", num[i], "Max =", maxi)
print ("largest number:", maxi)
print("total comparisons :", comp)
# sorting 
arr = num.copy()
n = len(arr)
for i in range (n-1):
    for j in range (n - 1 - i):
        if arr[j]> arr[j +1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
    print("After Pass", i+1, ":", arr)
print("sorted list:", arr)
