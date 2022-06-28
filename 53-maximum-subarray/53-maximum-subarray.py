class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mxsum=nums[0]
        currsum=0
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)):
            currsum+=nums[i]
            mxsum=max(mxsum,currsum)
            if currsum<0:
                currsum=0
        return mxsum
            