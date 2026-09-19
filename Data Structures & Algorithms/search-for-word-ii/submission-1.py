class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # DFS explores possible prefixes. While walking on the board, only continue path that match some prefix of the given words.
        # When the Trie node makrs the prefix is a complete word, record it in result.
        # use a visited set to avoid reusing the same cell in a single path. backtracking the cells for the next DFS recursive level
        
        # build a Trie from all words
        # running DFS startinf from every cell (r,c) with the Trie root.

        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or r == ROWS or c < 0 or c == COLS) or (r,c) in visited or board[r][c] not in node.children:
                return
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)

            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            visited.remove((r,c)) # !!! backtrack

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return list(res)
        # O(m * n * 4 * 3^(t-1) + s)