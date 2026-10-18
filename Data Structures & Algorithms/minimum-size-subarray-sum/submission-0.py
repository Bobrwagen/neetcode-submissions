class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curr = 0
        res = 0
        for i in range(len(nums)):
            curr += nums[i]
            while curr >= target:
                if res == 0:
                    res = i - l + 1
                res = min(res, i - l + 1)
                curr -= nums[l]
                l += 1
        return res