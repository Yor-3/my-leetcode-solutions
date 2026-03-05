class Solution:
    def insert(self, intervals, newInterval):

        i = 0
        n = len(intervals)

        # find insert position
        while i < n and intervals[i][1] < newInterval[0]:
            i += 1

        # merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            intervals.pop(i)
            n -= 1

        # insert merged interval
        intervals.insert(i, newInterval)

        return intervals