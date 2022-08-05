class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        nums.sort()
        for val in range(1,target+1):
            for num in nums:
                if num > val:
                    break 
                dp[val] += dp[val-num]
        return dp[-1]
        
        