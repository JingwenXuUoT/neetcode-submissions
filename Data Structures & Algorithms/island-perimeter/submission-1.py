class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
       row, col = len(grid), len(grid[0])
       directions = [(0,1), (0, -1), (1,0), (-1, 0)]
       visited = set()

       def bfs(r, c):
        res = 0
        queue = deque([(r,c)])
        visited.add((r,c)) # set can only add tuple

        while queue:
            x, y = queue.popleft()
            for dr, dc in directions:
                newr = x+dr
                newc = y+dc
                if newr<0 or newr>=row or newc<0 or newc>=col or grid[newr][newc] == 0:
                    res += 1 # interesting
                elif (newr, newc) not in visited :
                    visited.add((newr, newc))
                    queue.append((newr, newc))
        
        return res

       def dfs(i, j):
        if i<0 or i>=row or j<0 or j>=col or grid[i][j] == 0:
            return 1
        if (i, j) in visited:
            return 0
        visited.add((i, j))
        res = dfs(i, j+1)+dfs(i+1, j)+dfs(i-1, j)+dfs(i, j-1)
        return res

       for r in range(row):
            for c in range(col):
                if grid[r][c]:
                    return dfs(r, c)
       return 0
        

