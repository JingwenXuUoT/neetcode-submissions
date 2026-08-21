class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # longest[i][j] means the length of the lonegest common subsequence between str1 and str2 where i,j are the ending indexes of the subsequences of str1 and str2 respectively
        # transition rule: if str1[i] == str2[j], longest[i][j] = 1+longest[i-1][j-1], i+=1, j+=1; else longest[i][j] = max(longest[i][j-1], longest[i-1][j]), i+=1 when longest[i][j-1]>longest[i-1][j], otherwise j+=1
        # base case: if str1[0] == str2[0], longest[0][0] = 1, else longest[0][0] = 0
        # early return when i or j reach the end

        m = len(text1)
        n = len(text2)

        # longest = [[0] * m for _ in range(n)]
        # longest[0][0] = 1 if text1[0]==text2[0] else 0
        # the above lines also at risk of out of bound error

        # this algo is wrong because we need to fill in every cells in the 2D dp array
        # -> use a nested for loop
        # res = 0
        # i, j = 0, 0
        # while(i<m and j<n):
        #     if text1[i] == text2[j]:
        #         longest[i][j] = 1+longest[i-1][j-1]
        #         res = max(res, longest[i][j])
        #         i+=1
        #         j+=1
        #     else:
        #         longest[i][j] = max(longest[i][j-1], longest[i-1][j])
        #         res = max(res, longest[i][j])
        #         if longest[i][j-1]>longest[i-1][j]:
        #             i+=1
        #         else:
        #             j+=1
        
        # return res
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]
