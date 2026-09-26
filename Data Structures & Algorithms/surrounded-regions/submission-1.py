class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # start from every unvisited O, DFS traverse its neighbors and find surrounded region
        # early return if any of the O along the path touches the edges
        # if at the end of traverse, the region is really surrounded, change all Os into Xs
        m = len(board)
        n = len(board[0])
        # reverse the approach, check and sift out the region can be reached by the border Os, mark visited cells as '#'
        def dfs(r, c):
            if r<0 or r == m or c<0 or c == n or board[r][c] == "#" or board[r][c] == "X":
                return
            
            board[r][c] = "#" # mark visited
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
        
        # left, right
        for r in range(m):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][n-1] == "O":
                dfs(r, n-1)
        # top, bottom
        for c in range(1, n):
            if board[0][c] == "O":
                dfs(0, c)
            if board[m-1][c] == "O":
                dfs(m-1, c)
        
        # process the surrounded region
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"