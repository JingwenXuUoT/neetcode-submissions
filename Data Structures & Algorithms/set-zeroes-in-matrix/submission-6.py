class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        row0=1
        col0=1
        for r in range(m):
            if matrix[r][0] == 0:
                col0 = 0
                break
        for c in range(n):
            if matrix[0][c] == 0:
                row0 = 0
                break
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        for r in range(1, m):
            for c in range(1, n):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if col0 == 0:
            for r in range(m):# this is full range
                matrix[r][0] = 0
        if row0 == 0:
            for c in range(n):
                matrix[0][c] = 0      