def mergeSort(arr, left, right):
    if left >= right:
        return

    mid = (left + right) // 2
  
    mergeSort(arr, left, mid)
    mergeSort(arr, mid + 1, right) 
    leftArray = arr[left : mid + 1]
    rightArray = arr[mid + 1 : right + 1]
    merge(arr, leftArray, rightArray,left)


def merge(arr, left, right,l):
    i, j, k = 0, 0, l
    while i < len(left) and j < len(right):
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

    
test=[25,31,4,8,123,10,1,0,9,100,34]
mergeSort(test,0,len(test)-1)
print(test)