class solution():
    def binary_search(self,arr,k):
        n=len(arr)
        low=0
        high=n-1
        while(low<=high):
            mid=((low+high)//2)
            if k==arr[mid]:
                return mid
            elif k>arr[mid]:
                low=mid+1
            else:
                high=mid-1
        return -1
        

arr=[1,2,3,4,5,6,7]
k=5
new=solution()
print(new.binary_search(arr,k))

