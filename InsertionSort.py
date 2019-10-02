def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    # Driver code to test above


arr = [5.098, 0.6575, 7.675789, 3.89879, 8.898987, 9.8989, 4.887766, 2.8989, 6.9898, 1.0909]

insertionSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("%f" % arr[i])