class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 3 hash set, one pass
        # rows[r], digits seen in row r
        # cols[c], digits seen in column c
        # squares[(r // 3, c // 3)], digits in the 3*3 box
        # return False if current digit appears again in any of these sets
        # otherwise, add the current digit to the three sets
        # tc: O(n^2), sp: O(n^2)

        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                # for iterative and recursive problem, always first execute the edge cases and early termination/skip conditions
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]):
                    # a tuple can be a dictiionary key, but every element inside the tuple must also be hashable(immutable), e.g. integers, or strings, attention: list is not hashable
                    # because python evaluated chaining conditions from left to right, so to speed up the algo, always place the condition most likely yo be true to the left
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True