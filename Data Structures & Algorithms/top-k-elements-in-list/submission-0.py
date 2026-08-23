import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapu = defaultdict(int)
        for n in nums:
            mapu[n] += 1
        
        heap = []
        
        for num, count in mapu.items():
            heapq.heappush(heap, (-count, num))
        
        res = []
        for i in range(k):
            _, n = heapq.heappop(heap)
            res.append(n)
        return res 
        