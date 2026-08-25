class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # optimize O(n^2) extra space
        # two step rotation:
        # 1. reverse the matrix vertically
        # 2. transpose the reversed matrix
        # given a square matrix, transpose means over need to iterate over the upper triangular part.

        n = len(matrix)
        for r in range(n//2):
            temp_r = matrix[n-r-1]
            matrix[n-r-1] = matrix[r]
            matrix[r] = temp_r
        
        for r in range(n):
            for c in range(r, n):
                if r == c:
                    continue
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp
'''
[1,2,3],
[4,5,6],
[7,8,9]

[7,8,9],
[4,5,6],
[1,2,3],
'''

        