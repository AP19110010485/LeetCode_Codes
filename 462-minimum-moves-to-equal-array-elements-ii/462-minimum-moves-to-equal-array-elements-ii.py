class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums=sorted(nums)
        mid=nums[len(nums)//2]
        number=0
        for i in nums:
            number+=abs(i-mid)
        return number