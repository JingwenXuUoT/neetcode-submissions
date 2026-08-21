class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # filling a dp array from right to left
        # dp[i] meaning whether can jump from index i to the last index
        # transition rule: if nums[i] >= n-i, dp[i] = True; else, for j in range(i+1, i+nums[i]-1), if dp[j]==True, then dp[i]=True; else dp[i]=False
        # base case: dp[n-1] = True
        # return dp[0]
        # O(n*n)

        n = len(nums)
        dp = [False] * n
        dp[n-1] = True

        for i in range(n-2, -1, -1):
            if nums[i] >= n-i:
                dp[i] = True
                continue
            elif nums[i] > 0:
                for j in range(i+1, min(i+nums[i]+1, n)):
                    if dp[j]:
                        dp[i] = True
                        break

        return dp[0]