class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left=0
        mid=0
        high=len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[left],nums[mid]=nums[mid],nums[left]
                mid+=1
                left+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[high],nums[mid]=nums[mid],nums[high]
                high-=1
        """
        Do not return anything, modify nums in-place instead.
        """
        