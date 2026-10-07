"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        newInter = sorted(intervals, key=lambda interval: interval.start)
        for i in range(len(newInter) - 1):
            if newInter[i].end > newInter[i + 1].start:
                return False
        return True