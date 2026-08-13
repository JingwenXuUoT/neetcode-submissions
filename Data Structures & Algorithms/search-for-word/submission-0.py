class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        rows, cols = len(board), len(board[0]) 

        def wordSearch(visited, word_idx, path, row, col):
            if path == word:
                return True
            
            if (row < 0 or row >= rows or col < 0 or col >= cols
                or (row, col) in visited or board[row][col] != word[word_idx]):
                return False

            visited.add((row, col))
            cur_res = False
            for d in directions:
                nei_row = row + d[0]
                nei_col = col + d[1]
                if wordSearch(visited, word_idx+1, path+board[row][col], nei_row, nei_col):
                    cur_res = True
                    break
                
            visited.remove((row, col))

            return cur_res

        for r in range(rows):
            for c in range(cols):
                visited = set()
                if wordSearch(visited, 0, "", r, c):
                    return True
        
        return False

            