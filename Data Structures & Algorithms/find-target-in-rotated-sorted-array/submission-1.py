class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minInd = self.findMin(nums)
        def binSearch(l, r, target):
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1
        
        if target <= nums[-1]:
            return binSearch(minInd, len(nums)-1, target)
        else:
            return binSearch(0, minInd-1, target)


    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return l