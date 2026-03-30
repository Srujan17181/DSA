arr=[5, 7,7,8,8, 8, 10]


def first_occurance(arr,target):
    low=0
    high=len(arr)-1
    ans=-1
    while(low<=high):
        mid=((low+high)//2)-1
        if arr[mid]==target:
            ans=mid
            high=mid-1 
        elif arr[mid]<=target:
            low=mid+1
        else:
            high=mid-1
    return ans



def last_occurance(arr,target):
    low=0
    high=len(arr)-1
    ans=-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]==target:
            ans=mid
            low=mid+1
        elif arr[mid]<=target:
            low=mid+1
        else:
            high=mid-1
    return ans



print(first_occurance(arr,8),last_occurance(arr,8))
