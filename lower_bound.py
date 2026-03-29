
def lowerBound(nums, x):
    n=len(nums)
    low=0
    high=n-1
    while(low<=high):
        mid=((low+high)//2)
        if nums[mid]>=x:
            return mid
        else:
            low=mid+1
    return n

arr=[1,2,2,3]
print(lowerBound(arr,2))

