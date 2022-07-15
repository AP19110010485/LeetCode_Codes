class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.row, self.col = len(grid), len(grid[0])
        ans = 0
        
        def solve(i, j):
            if grid[i][j]==1:
                grid[i][j] = 0
                left, up, right, down = 0, 0, 0, 0
                if j>0: 
                    left = solve(i, j-1)
                if i>0:
                    up = solve(i-1, j)
                if j<self.col-1:
                    right = solve(i, j+1)
                if i<self.row-1:
                    down = solve(i+1, j)
                return 1+left+up+right+down
            return 0
        
        for i in range(self.row):
            for j in range(self.col):
                if grid[i][j]==1:
                    ans = max(ans, solve(i, j))
        return ans
        