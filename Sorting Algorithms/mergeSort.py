def mergeSort(arr,left, right):
    if left<right:
        mid=(left+right)//2
        leftArray=arr[:mid]
        rightArray=arr[mid:len(arr)]
        mergeSort(arr,left,mid)
        mergeSort(arr,mid+1,right)
        merge(arr, leftArray, rightArray)

def merge(arr,left,right):
     i,j=0,0
     while(i<len(left) and j<len(right)):
         if(left[i]<right[j]):
             arr[i]=left[i]
             i+=1
         else:
             arr[j]=left[j]
             j+=1
     while(i<len(left)):
         arr[i]=left[i]
         i+=1
     while(j<len(right)):
         arr[j]=right[j]
         j+=1
    