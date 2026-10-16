class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(filter(lambda  x: x > 0, nums))
        if not nums or min(nums) > 1:
            return 1
        curr = None
        for n in nums:
            if n + 1 not in nums:
                if not curr:
                    curr = n + 1
                else:
                    curr = min(curr, n + 1)
        return 1 if curr is None else curr