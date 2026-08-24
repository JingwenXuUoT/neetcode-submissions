"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # this need to construct  a number line representng start and end times
        # the number of room required is the maximum number of overlapping meetings at any point on the number line
        # creae two arrays for all the starts and the ends
        # two pointers s,e 
        # one maintained variable count
        # count is the current number of active meetings
        if not intervals:
            return 0

        # start_points = []
        # end_points = []
        # for interval in intervals:
        #     start_points.append(interval.start)
        #     end_points.append(interval.end)
        # start_points.sort()
        # end_points.sort()
        #  more simple codes:
        start_points = sorted(i.start for i in intervals)
        end_points = sorted(i.end for i in intervals)

        s = 0
        e = 0
        count = 0
        res = 0

        while s < len(intervals):
            if start_points[s] < end_points[e] :
               s+=1
               count+=1
            else:
                # a meeting ends meaning end_points[e] is the smallest end-time not yet processed, once compared it and it turns out to be <= the next start time, free up the room it was occupying by decrementing count and moving e forward so it now points at the enxt smallest unpreocessed end time.
                e+=1
                count -= 1
            res = max(res, count)
        return res
