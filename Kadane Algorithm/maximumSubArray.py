def maxSub(arr):
    maxGlobal=arr[0]
    current=maxGlobal
    for i in range(1,len(arr)):
        current=arr[i]