class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific, atlantic = set(), set() # one shared visited set that every border-call dfs call adds into it
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]

        def dfs(row, col, visited, prev_height):
            if row<0 or row>rows-1 or col<0 or col>cols-1 or (row, col) in visited or heights[row][col] < prev_height:
                return
            visited.add((row, col))
            for d in dirs:
                dfs(row+d[0], col+d[1], visited, heights[row][col])


        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols-1, atlantic, heights[r][cols-1])
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows-1, c, atlantic, heights[rows-1][c])

        return [[r,c] for r in range(rows) for c in range(cols) if (r,c) in pacific and (r,c) in atlantic]