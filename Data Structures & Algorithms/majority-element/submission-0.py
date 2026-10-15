class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        res = 0
        resNum = None
        for i in range(len(nums)):
            n = nums[i]
            counts[n] += 1
            if counts[n] >= res:
                res = counts[n]
                resNum = nums[i]
        return resNum
        