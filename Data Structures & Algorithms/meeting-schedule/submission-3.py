"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # check if there's overlap intervals
        # intervals.sort()
        # must use a lambda function to sort this format of interval list
        intervals.sort(key=lambda x: x.start)
        if len(intervals) == 0:
            return True
        # prevEnd = intervals[0].end
        # only need to check adjacent intervals
        # prevEnd is not needed, cause we only need to find the first overlap
        for i in range(1, len(intervals)):
            if intervals[i].start<intervals[i-1].end:
                return False
        return True