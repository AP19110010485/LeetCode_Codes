class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        hm1 = Counter(nums)
        hm2 = defaultdict(int)
        
        for num in nums:
            if hm1[num] == 0: continue
            
            if num - 1 in hm2 and hm2[num - 1] > 0:
                hm2[num - 1] -= 1
                hm2[num] += 1
            
            elif num + 1 in hm1 and num + 2 in hm1 and hm1[num + 1] > 0 and hm1[num + 2] > 0:
                hm2[num + 2] += 1
                hm1[num + 1] -= 1
                hm1[num + 2] -= 1
            
            else:
                return False
            
            hm1[num] -= 1
        
        return True
        