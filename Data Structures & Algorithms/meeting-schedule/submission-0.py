"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        timeslots = [0] * 1000001
        for interval in intervals:
            for i in range(interval.start, interval.end):
                if timeslots[i] != 0:
                    return False
                timeslots[i] = 1
        return True