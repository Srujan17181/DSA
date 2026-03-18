arr= [5, 4, 3, 2, 1]

profit=0

for i in range(len(arr)):
    profit1=0
    for j in range(i,len(arr)):
        if arr[j]>arr[i]:
            profit1=arr[j]-arr[i]
            profit=max(profit1,profit)



print(profit)