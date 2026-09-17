class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        fresh = 0
        time = 0
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        while fresh > 0 and q:
            size = len(q)
            for i in range(size):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r+dr
                    nc = c+dc
                    if nr<0 or nr==m or nc<0 or nc==n or grid[nr][nc] in (0,2):
                        continue
                    grid[nr][nc] = 2
                    q.append((nr,nc))
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1