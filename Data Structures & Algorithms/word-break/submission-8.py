class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # # turn wordDict into set for O(1) lookup
        # wordSet = set(wordDict)
        # # get the maximum length of the wordDict
        # t = 0
        # for w in wordDict:
        #     t = max(t, len(w))
        # # use hashmap to remeber the same substring result
        # memo = {n : True}

        # def match(i):
        #     if i in memo:
        #         return memo[i]
        #     if i == len(s):
        #         return True
            
        #     for j in range(i, min(n, i+t)):
        #         # for new ending s[i:j], we do not need to check j one position by one position
        #         if s[i:j+1] in wordSet:
        #             if match(j + 1):
        #                 memo[i] = True
        #                 return True
        #     memo[i] = False
        #     return False
        
        # return match(0)
        
        # method 2: Bottom-up DP
        # dp[i] means whther the substring s[i:] can be segmented
        dp = [False] * (n +1)
        dp[0] = True

        for i in range(1, n+1):
            for w in wordDict:
                if (i - len(w) >= 0 and s[i-len(w):i] == w):
                    dp[i] = dp[i-len(w)]
                if dp[i]:
                    break # break the inner for loop
        return dp[n]
        