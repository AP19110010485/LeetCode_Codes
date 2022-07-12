class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
         #recursive solution
 
        value = sum(matchsticks)
        if value < 4 or value % 4:
            return False
        edge = value // 4
        
        nums = []
        for n in matchsticks:
            if n > edge:
                return False
            if n < edge:
                nums.append(n)
        if nums == []:  #four element is the same size as edge
            return True
        k = 4 - (len(matchsticks) - len(nums))  #how many edges we still need to solve
        nums.sort(reverse=True)
        used = [False] * len(nums)
        
        def helper(nums, used, i, edge, sum, k):
            if k == 1:        #found all the edges
                return True
            
            while i < len(nums):
                if not used[i]:
                    used[i] = True
                    if sum + nums[i] < edge and helper(nums, used, i + 1, edge, sum + nums[i], k):
                        return True
                    if sum + nums[i] == edge and helper(nums, used, 0, edge, 0, k - 1):
                        return True
                    used[i] = False
                    while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                        i += 1
                    if sum == 0:
                        return False
                i += 1
            return False
        
        return helper(nums, used, 0, edge, 0, k)
        