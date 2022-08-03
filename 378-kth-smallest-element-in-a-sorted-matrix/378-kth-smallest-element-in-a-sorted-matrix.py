class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lst = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                lst.append(matrix[i][j])
        lst.sort()       
        return lst[k-1]