def mergeSort(arr,left, right):
    while left<right:
        mid=(left+right)//2
        
        mergeSort(arr,left,mid)
        mergeSort(arr,mid+1,right)
        merge(arr, left,mid, right)