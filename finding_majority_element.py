#moores voting algorithms
arr=[7, 0, 0, 1, 7, 7, 2, 7, 7]


el=0
count=0

for i in range(len(arr)):
    if count==0:
        el=arr[i]
        count=1
    elif arr[i]==el:
        count+=1
    else:
        count-=1

count1=0
for i in range(len(arr)):
    if arr[i]==el:
        count1+=1

if(count1>len(arr)/2):
    print(el)

