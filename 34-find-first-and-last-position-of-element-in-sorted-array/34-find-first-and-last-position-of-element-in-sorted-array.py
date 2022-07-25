class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        c=[]
        d=[-1,-1]
        if target not in nums or len(nums)==0:
            return d
        else:
            for i in range(len(nums)):
                if nums[i]==target:
                    c.append(i)
            
            e=[]
            e.append(c[0])
            k=c.pop()
            e.append(k)
            return e
            
        
        
        