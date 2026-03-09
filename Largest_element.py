class Solution:
    def largest_element(self,nums):
        largest=nums[0]
        for i in range(len(nums)):
            if largest<nums[i]:
                largest=nums[i]

        return largest

sol=Solution()
print(sol.largest_element([-3,-3,0,1,-8]))

