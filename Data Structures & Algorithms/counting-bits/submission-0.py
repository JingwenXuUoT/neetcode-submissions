class Solution:
    def countBits(self, n: int) -> List[int]:
        # bit manipulation + dynamic programming
        # since every binary number can be represented as highestPowerOfTwo <= i + remainder
        # and the first part have only one 1, the remainder can be found by dp[i-offset]
        # dp[i] = 1+ dp[i-offset], dp[i] means the number of set bits in i
        # offset starts at 1 and updates when encountering a power of 2->if offset * 2 == current number, then update offset
        dp = [0] * (n+1)
        offset = 1
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i-offset]
        return dp

        