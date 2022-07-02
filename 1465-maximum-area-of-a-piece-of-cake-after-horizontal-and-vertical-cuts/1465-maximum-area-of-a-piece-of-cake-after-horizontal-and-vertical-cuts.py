class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        horizontalCuts.append(h)
        verticalCuts.append(w)
        
        horizontalCuts.insert(0, 0)
        verticalCuts.insert(0, 0)
        
        length = 0
        for i in range(len(horizontalCuts)-1):
            length = max (length, horizontalCuts[i+1] - horizontalCuts[i])
            
        breadth = 0
        for j in range(len(verticalCuts)-1):
            breadth = max (breadth, verticalCuts[j+1] - verticalCuts[j])
            
        return ((length * breadth) % (pow(10, 9) + 7))

        
        
        
        