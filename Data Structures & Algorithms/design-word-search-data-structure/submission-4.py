class WordNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = WordNode()
            cur = cur.children[ch]
        cur.is_word = True

    def search(self, word: str) -> bool:
        # need a helper to do the recursive search, callbacks are needed
        def dfs(i, node):
            if i == len(word):
                return node.is_word
            ch = word[i]
            if ch == '.':
                for child in node.children.values():
                    if(dfs(i+1, child)):
                        return True
                return False
            else:
                if ch not in node.children:
                    return False
                return dfs(i+1, node.children[ch])
            #     node = node.children[ch]
            # return node.is_word

        return dfs(0, self.root)
