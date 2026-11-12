class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for i, ch in enumerate(order):
            order_map[ch] = i

        for i in range(1, len(words)):
            w1 = words[i-1]
            w2 = words[i]
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                if w1[j] != w2[j]:
                    if order_map[w1[j]]>order_map[w2[j]]:
                        return False
                    break # once the differ moment finish the check, can move on to the next pair, which guarantees that "disk" is smaller than "dog"
        return True
                