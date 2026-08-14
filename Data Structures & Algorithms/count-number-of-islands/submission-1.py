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
# alternatives:
# visited = set()
# def findReachables(row, col):
#     if (row < 0 or row > rows-1 or col < 0 or col > cols-1
#             or grid[row][col] == "0" or (row, col) in visited):
#         return
#     visited.add((row, col))

# in production, recursive DFS might fails on large grid, since DFS chian exceeds Python's recursion limit(~1000 by default), an explict stack works:
'''
def findReachables(row, col):
    stack = [(row, col)]
    while stack:
        r, c = stack.pop()
        if r < 0 or r > rows-1 or c < 0 or c > cols-1 or grid[r][c] == "0":
            continue
        grid[r][c] = "0"
        stack.extend([(r-1,c), (r+1,c), (r,c-1), (r,c+1)])
'''