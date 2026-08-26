class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            if (1<<i) & n:
                # creating a mask with 1<<i
                # & can be used to test whether that bit is set in n
                res+=1
        return res