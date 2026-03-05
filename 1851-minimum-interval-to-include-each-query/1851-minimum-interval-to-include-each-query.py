import heapq

class Solution:
    def minInterval(self, intervals, queries):

        intervals.sort()
        queries_sorted = sorted([(q,i) for i,q in enumerate(queries)])

        res = [-1]*len(queries)

        heap = []
        i = 0

        for q,idx in queries_sorted:

            # add valid intervals
            while i < len(intervals) and intervals[i][0] <= q:
                left,right = intervals[i]
                size = right-left+1
                heapq.heappush(heap,(size,right))
                i += 1

            # remove invalid intervals
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            if heap:
                res[idx] = heap[0][0]

        return res