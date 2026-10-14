class Solution:
    def merge(self, num1: List[int], m: int, num2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # start to fill num1 from the tail, there's already empty space
        # start a pointer from the back, get the largest value by comparing the two last vlaues from num1 and num2
        last = m + n -1
        while m > 0 and n > 0:
            if num1[m-1] > num2[n-1]:
                num1[last] = num1[m-1]
                m -= 1
            else:
                num1[last] = num2[n-1]
                n -= 1
            last -= 1
        
        # one last edge case: the smallest value is the remanings in num2
        while n > 0:
            num1[last] = num2[n-1]
            n, last = n-1, last-1

