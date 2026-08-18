class Solution:
    def longestPalindrome(self, s: str) -> str:
        # store the start index of the longest palindrome string
        # global variable: max_length
        # dp[i][j] is True if the substring s[i..j] is a palindrome
        # the substring s[i..j] is a palindrome is s[i] == s[j] and s[i+1][j-1] is a palindrome
        # edge cases: j-1<=2, matching ends is enough
        # fill dp from bottom to top, dp[i+1][j-1] is there when computing dp[i][j]
        # while filling, keep track of the longest palindrom so far

        resIdx = 0
        resLen = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j]  = True
                    if resLen < (j-i+1):
                        resIdx = i
                        resLen = j-i+1
        
        return s[resIdx: resIdx+resLen]