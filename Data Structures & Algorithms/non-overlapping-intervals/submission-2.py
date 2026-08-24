class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
                continue
            else:
                prevEnd = min(prevEnd, end)
                res += 1
            
        return res
'''
prevEnd = 2, 
res = 0
'''