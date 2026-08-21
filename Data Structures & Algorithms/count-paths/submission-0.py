class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # iterate from the top left to the bottom right
        # path[i][j] means the total unique path from 0,0 to i,j
        # path[i][j] = path[i-1][j] + path[i][j-1]
        # base case: path[0][0]=1, path[0][j] =1, path[i][0]=1

        path = [[0] * n for _ in range(m)]

        for i in range(m):
            path[i][0] = 1
        for j in range(1,n):
            path[0][j] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                path[i][j] = path[i-1][j] + path[i][j-1]

        return path[m-1][n-1]   