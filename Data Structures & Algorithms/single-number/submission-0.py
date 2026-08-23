class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        current = 0
        for num in nums:
            current = current ^num
        return current
        