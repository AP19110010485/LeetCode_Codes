class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        
        #taking extra array so we can store max values in it
        # we will also take care of range
        list_index = [0]
        
        #looping from 1st element to last element in nums array
        for i in range(1,n):
            
            #we need only those index which are between
            # i-k-1 to i-1
            # we are removing all unnecessary index
            while i-list_index[0]>k and len(list_index)>0:
                curr_index = list_index.pop(0)
            
            ##simple assigning max value
            nums[i] = nums[i]+nums[list_index[0]]
            #print(nums[i])
            
            
            #we need only max values index that's why
            #removing all those value index which are lower than or equal to our new nums[i]
            while list_index and nums[list_index[-1]]<= nums[i]:
                list_index.pop()
            
            #appendin new index in array
            #we already remove low values so
            #0th index of list_index automatic becomes max value index
            list_index.append(i)
            
        #print(nums)
        return nums[-1]
        