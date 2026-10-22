import heapq

class TimeMap:

    def __init__(self):
        self.heap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.heap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        lis = self.heap[key]
        if not lis:
            return ""
        l,r = 0, len(self.heap[key]) - 1
        res = -1
        while l <= r:
            mid = (l+r) // 2
            stamp = lis[mid][1]
            if stamp <= timestamp:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        if res == -1:
            return ""
        return lis[res][0]
