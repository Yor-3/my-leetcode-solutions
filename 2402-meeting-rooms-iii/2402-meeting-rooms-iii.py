from heapq import heappop, heappush
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x:x[0])
        available = [i for i in range(n)]
        used = []   #(end, room)
        count = [0] * n

        for start, end in meetings:
            while used and used[0][0] <= start:
                _, room = heappop(used)
                heappush(available, room)
            
            if available:
                room = heappop(available)
                heappush(used, (end, room))
                count[room] += 1
            else:
                used_end, room = heappop(used)
                new_end = used_end + (end-start)
                heappush(used, (new_end, room))
                count[room] += 1
        
        return count.index(max(count))