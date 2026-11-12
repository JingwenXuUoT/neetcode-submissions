class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # start from every non-visited land grid
        # DFS from it, count the connected area
        # maintain a global maxArea
        # update maxArea at the end of every DFS
        # change the grid to -1 if visited
        # O(n*m), O(1)

        n = len(grid)
        m = len(grid[0])
        directions = [[-1,0], [1,0], [0,-1], [0,1]]

        def dfs(row, col):
            if row<0 or row>=n or col<0 or col>=m or grid[row][col] == -1 or grid[row][col] == 0:
                    return 0
            grid[row][col] = -1
            area = 1
            for dr, dc in directions:
                area += dfs(row + dr, col + dc)
            return area

        maxArea = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    maxArea = max(maxArea, area)
        
        return maxArea
