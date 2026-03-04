class solution():
    def majority_elements(self,nums):

        candidate=nums[0]
        count=0
        for el in nums:
            if candidate==el:
                count+=1
            else:
                if(count==0):
                    candidate=el
                    count+=1
                else:
                    count-=1
                
        return candidate

sol=solution()
print(sol.majority_elements([3,2,3,2,2]))