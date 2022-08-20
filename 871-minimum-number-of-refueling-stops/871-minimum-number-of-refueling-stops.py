class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        cur = startFuel
        stops = 0
        heap = []
        stations.append([target, 0])
        for pos, fuel in stations:
            while(heap and pos > cur):
                this = -heapq.heappop(heap)
                cur += this
                stops += 1
            if(pos > cur): 
                return -1
            heapq.heappush(heap, -fuel)
        return stops