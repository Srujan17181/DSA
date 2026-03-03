# Two sum problem 


class solution():
    def TwoSum(self,array,target):
        for i in range(len(a)):
            for j in range(i,len(a)-1):
                if a[i]+a[j+1]==target:
                    return i,j+1
                

a=[3,2,3]
target=6
SOL=solution() 
print(SOL.TwoSum(a,target))
