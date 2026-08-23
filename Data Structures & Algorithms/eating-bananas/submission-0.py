class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        result = right
        def works(n):
            res = 0
            for p in piles:
                res += math.ceil(p / n)
            return True if res <= h else False
        while left <= right:
            mid = (left + right) // 2
            new = works(mid)
            print("--- : ", new, mid, result)
            if not new:
                left = mid + 1
            else:
                result = min(mid, result)
                right = mid - 1
        return result
        
        