import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-n for n in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            heavy = heapq.heappop(heap)
            sec_hev = heapq.heappop(heap)
            diff = abs(heavy-sec_hev)
            if diff > 0:
                heapq.heappush(heap, -diff)
        return -heap[-1] if heap else 0


