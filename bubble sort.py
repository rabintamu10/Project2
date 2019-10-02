def bubbleSort(arr):
    time = 0
    for pass_num in range(len(arr)-1, 0, -1):
        for i in range(pass_num):
            if arr[i] > arr[i+1]:
                time = time + 1
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

    return(time)

#import time module



arr = [5.098, 0.6575, 7.675789, 3.89879, 8.898987, 9.8989, 4.887766, 2.8989, 6.9898, 1.0909]
bubbleSort(arr)
print(arr)