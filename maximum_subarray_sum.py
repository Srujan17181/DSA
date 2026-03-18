#kadene's algo 
arr=[2,3,5,-2,7,-4]

# brute force approach 
maxi=0
for i in range(len(arr)):
    for j in range(i,len(arr)):
        sum=0
        for k in range(i,j):
            sum+=arr[k]
            maxi=max(sum,maxi)


# better solution 
maxi=0
for i in range(len(arr)):
    sum=0
    for j in range(i,len(arr)):
        sum+=arr[j]
        maxi=max(sum,maxi)

# optimal solution 

maxi=0
sum=0
ansstart=-1
ansend=-1

for i in range(len(arr)):
    if (sum==0):
        start=i
    sum+=arr[i]
    if sum>maxi:
        maxi=sum
        ansstart=start
        ansend=i
    if sum<0:
        sum=0

print(arr[ansstart:ansend+1])

