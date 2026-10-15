class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr = len(nums)
        index = 0
        ptr = 0
        for i in range(curr):
            if nums[ptr] == val:
                nums.pop(ptr)
                curr -= 1
            else:
                ptr += 1
        return curr