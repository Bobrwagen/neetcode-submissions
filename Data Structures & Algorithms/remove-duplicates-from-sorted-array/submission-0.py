class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        m = len(nums)
        left = 0
        while left < m - 1:
            if nums[left+1] == nums[left]:
                m -= 1
                nums.pop(left)
            else:
                left += 1
        return left + 1