class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1, max(piles)
        ans = -1
        while l <= r:
            mid = (l+r) // 2
            rate = 0
            for p in piles:
                rate += math.ceil(p/mid)
            if rate <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans