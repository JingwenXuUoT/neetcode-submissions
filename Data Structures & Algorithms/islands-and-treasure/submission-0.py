class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # BFS, count the accumlated steps took from entrance land cell to the nearest treasure chest. assign the value to the land cell
        m = len(grid)
        n = len(grid[0])
        # start from every treasure cell, change the value if BFS traverse to a INF cell along the way-> won't revisit a cell-> multi-source BFS
        queue = deque()
        visited = set()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    # grid[r][c] = -2 # marked as visited
                    # here, this duplication does not work, because grid value need to be changed to dist and dedup at the same time, using a constant dedup value is not possible
                    visited.add((r,c))
                    queue.append((r,c))
        
        dist = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while queue:
            size = len(queue)
            for i in range(size):
                r, c = queue.popleft()
                grid[r][c] = dist
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (nr, nc) in visited or nr<0 or nr>=m or nc<0 or nc>=n or grid[nr][nc] == -1:
                        continue
                    visited.add((nr, nc))
                    queue.append([nr, nc])
            dist += 1