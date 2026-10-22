class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = math.ceil(len(weights) / days) * max(weights)
        ans = -1
        while l <= r:
            mid = (l+r) // 2
            curr = 1
            currCap = 0
            for w in weights:
                if currCap + w > mid:
                    curr += 1
                    currCap = w
                else:
                    currCap += w
            if curr <= days:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans