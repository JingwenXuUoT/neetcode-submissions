class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:    
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.is_word = True
            

    def search(self, word: str) -> bool:
        node = self._traverse(word)
        return node is not None and node.is_word
        # the end-of-word marker is not set to true when reach the end of the word, return False

    def startsWith(self, prefix: str) -> bool:
        return self._traverse(prefix) is not None
    
    def _traverse(self, s: str):
        cur = self.root
        for ch in s:
            if ch not in cur.children:
                return None
            cur = cur.children[ch]
        return cur
        
        