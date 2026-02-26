class Solution:
    def mostFrequentElement(self, nums):
        hash_num=[0]*100
        for i in range(len(nums)):
            hash_num[nums[i]]+=1

        maxi=max(hash_num)
        high_freq=hash_num.index(maxi)
        return high_freq
