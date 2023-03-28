def findMinSumLength(array,target):
    currentSum=0
    minLength=10000000000000000000000000000000000000000000000000000000000000
    startWindow=0
    for endWindow in range(len(array)):
        currentSum+=array[endWindow]
        if currentSum>=target:
             minLength=min(minLength,(endWindow-startWindow)+1)
             currentSum-=array[(endWindow-startWindow)-endWindow]
             startWindow+=1
    return minLength


arr=[2,3,4,5,6,7,1,-1,3]
print(findMinSumLength(arr,14))