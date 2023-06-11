def mergeSort(arr):
    left=0
    right=len(arr)-1
    while left<right:
        mid=(left+right)//2
        leftArray=arr[:mid]
        rightArray=arr[mid:len(arr)]
        left+=1
        right-=1
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
    
test=[25,31,4,8,123,10,1,-23,9,100,34]
mergeSort(test)
print(test)