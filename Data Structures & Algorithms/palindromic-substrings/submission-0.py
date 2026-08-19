class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        dp = [[False] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i,n):
                # the order of dp filling is from bottom left to top right
                if s[i] == s[j] and (j-i<=2 or dp[i+1][j-1]):
                    # j-i<=2 should write before dp[i+1][j-1] to avoid out of bound error
                    dp[i][j] = True
                    res += 1
        
        return res