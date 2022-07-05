class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        ans=1
        count=1
        if len(nums)==0:
            return 0
        
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]+1:
                count+=1
                ans=max(ans,count)
            else:
                count=1
        return ans
            
        