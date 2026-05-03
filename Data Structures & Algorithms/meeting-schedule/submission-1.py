"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda intervals : intervals.start)
        for i in range(0, len(intervals) - 1):
            if intervals[i].end <= intervals[i + 1].start:
                continue
            return False
        return True