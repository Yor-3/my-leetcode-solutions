import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        # available rooms heap (min-heap)
        available = [i for i in range(n)]
        heapq.heapify(available)

        # used rooms heap (min-heap of (end time, room number))
        used = []
        
        # count of meetings per room
        count = [0] * n

        for start, end in meetings:
            # free up rooms whose meetings have already ended
            while used and used[0][0] <= start:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                heapq.heappush(used, (end, room))
            else:
                endtime, room = heapq.heappop(used)
                duration = end - start
                new_end = endtime + duration
                heapq.heappush(used, (new_end, room))
            
            count[room] += 1

        # return the room with the most meetings (smallest room number if tie)
        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i
