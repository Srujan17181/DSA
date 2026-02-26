arr=[13,46,24,52,20,9]
for i in range(len(arr)-1):
    a=min(arr[i:])
    x=arr.index(a)
    y=i
    arr[x],arr[y]=arr[y],arr[x]
print(arr)

#multiple looping 
# first loop for swap the numbers
# second loop for 
for i in range(len(arr)-1):
    mini=i
    for j in range(i,len(arr)-1):
        if(arr[j]<arr[mini]):
            mini=j

    arr[mini],arr[i]=arr[i],arr[mini]

print(arr)
            


