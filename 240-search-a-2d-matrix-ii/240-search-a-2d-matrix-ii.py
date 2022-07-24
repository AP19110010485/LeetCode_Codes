class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])
        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == target:
                    return True
        return False
        