def mergeSort(arr,left, right):
    while left<right:
        mid=(left+right)//2
        mergeSort(arr,mid+1,right)
        mergeSort(arr,left,mid-1)