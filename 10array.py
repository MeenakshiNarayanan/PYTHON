arr = [21,11,31,13,11]
for i in range(0, len(arr)):
    for k in range(i+1, len(arr)):
        if arr[i] == arr[k]:
            print("Duplicate element in the given array: ", arr[k])
