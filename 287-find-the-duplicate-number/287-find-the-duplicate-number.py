class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a = sorted(nums)
        for i in range(len(nums)-1):
            if a[i] == a[i+1]:
                return a[i]