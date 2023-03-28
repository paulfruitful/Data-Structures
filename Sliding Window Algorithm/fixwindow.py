def findMinSum(array,k):
    current=0
    minSum=10000000000000000000000000000000000000000000000000
    start=0
    for i in range(len(array)-1):
        current+=array[i]
        if (i-start)==k-1:
            minSum=min(minSum,current)
            current-=array[i-(k-1)]            
            start+=1
    return minSum

arr=[2,3,4,5,6,7,1,-1,3]
print(findMinSum(arr,2))