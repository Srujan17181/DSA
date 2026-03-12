arr=[1,4,5,6,7]

def linear_search(nums,num):
    for i in range(len(nums)):
        if nums[i]==num:
            return i
        
print(linear_search(arr,6))