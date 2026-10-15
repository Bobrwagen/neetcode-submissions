class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def swap(nums, left, right):
            nums[left], nums[right] = nums[right], nums[left]
        def partition(nums, left, right):
            mid = (left + right) // 2
            swap(nums, mid, right)
            pivot = nums[right]
            i = left - 1;
            for j in range(left, right):
                if nums[j] < pivot:
                    i += 1
                    swap(nums, i, j)
            swap(nums, i+1, right)
            return i+1
        def quickSort(nums, start, end):
            if start > end:
                return
            pivot = partition(nums, start, end)
            quickSort(nums, start, pivot - 1)
            quickSort(nums, pivot + 1, end)
        quickSort(nums, 0, len(nums) - 1)
        return nums


