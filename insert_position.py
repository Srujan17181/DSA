def searchInsert(nums, target):
    n=len(nums)
    low=0
    high=n-1
    while(low<=high):
        mid=((low+high)//2)
        if target==nums[mid]:
            return mid
        elif target>nums[mid]:
            low=mid+1
        else:
            high=mid-1
    
    return low
arr=[1,3,5,6]
print(searchInsert(arr,2))