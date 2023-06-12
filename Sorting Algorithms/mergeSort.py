def mergeSort(arr,left, right):
    if left>=right:
        return None
    if left<right:
        mid=(left+right)//2
        leftArray=arr[:mid]
        rightArray=arr[mid:len(arr)]
        mergeSort(arr,left,mid)
        mergeSort(arr,mid+1,right)
        merge(arr, leftArray, rightArray)

def merge(arr, left, right):
    i, j, k = 0, 0, 0
    while i < len(left)-1 and j < len(right)-1:
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    
test=[25,31,4,8,123,10,1,-23,9,100,34]
mergeSort(test,0,len(test)-1)
print(test)