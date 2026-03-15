arr=[10, 5, 2, 7, 1, 9] #k=15
k=15

left=0
right=0
k=15
maxlength=0
n=len(arr)
sum=arr[0]
while(right<n):
    while(left<=right and sum>k):
        sum-=arr[left]
        left_=1
    if (sum==k):
        maxlength=max(maxlength,right-left)

    right+=1
    if(right <n ):
        sum+=arr[right]

print(maxlength)





