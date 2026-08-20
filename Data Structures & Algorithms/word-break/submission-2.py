class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # turn wordDict into set for O(1) lookup
        wordSet = set(wordDict)
        # use hashmap to remeber the same substring result
        memo = {n : True}

        def match(i):
            if i in memo:
                return memo[i]
            
            for w in wordDict:
                if ((i+len(w)) <= n and s[i:i+len(w)]==w):
                    if match(i + len(w)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        
        return match(0)
            
        