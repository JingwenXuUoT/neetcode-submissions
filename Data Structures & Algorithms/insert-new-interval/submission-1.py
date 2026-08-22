class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                res.append(interval)
        interval_idx = len(res)-1
        count = 0
        for i in range(interval_idx+1,len(intervals)):
            if intervals[i][0]<=newInterval[1]:# general condition of overlapping
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
                count+=1
            else:
                break
        res.append(newInterval)
        interval_idx += count
        interval_idx+=1
        while interval_idx<len(intervals):
            res.append(intervals[interval_idx])
            interval_idx+=1
        
        return res


            