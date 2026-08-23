class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        cursum = 0
        for n in nums:
            if cursum < 0:
                cursum = n
            else:
                cursum += n
            res = max(cursum, res)
        return res
        
        