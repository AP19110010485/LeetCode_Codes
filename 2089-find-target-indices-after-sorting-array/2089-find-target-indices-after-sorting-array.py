class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        p=sorted(nums)
        c=[]
        for i in range(len(p)):
            if p[i]==target:
                c.append(i)
        return c
                
        