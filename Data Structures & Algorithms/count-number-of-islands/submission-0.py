class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # use 1->0 marker to indicate visited cells
        rows = len(grid)
        cols = len(grid[0])
        num_islands = 0

        def findReachables(row, col):
            if row<0 or row>rows-1 or col<0 or col>cols-1 or grid[row][col] == "0":
                return
            
            grid[row][col] = "0"
            findReachables(row-1, col)
            findReachables(row+1, col)
            findReachables(row, col-1)
            findReachables(row, col+1)

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    findReachables(r,c)
                    num_islands += 1
        
        return num_islands