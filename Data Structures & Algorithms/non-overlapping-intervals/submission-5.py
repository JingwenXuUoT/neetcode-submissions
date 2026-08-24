class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] >= prevEnd:
                prevEnd = interval[1]
            else:
                prevEnd = min(prevEnd, interval[1])
                res += 1
            
        return res
'''
prevEnd = 2, 
res = 0
'''