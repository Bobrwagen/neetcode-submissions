class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j-1] == nums[j]:
                    continue
                left = j+1
                right = n-1
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] == target:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        left += 1
                        while left < n and nums[left-1] == nums[left]:
                            left += 1
                        right -= 1
                        while right > left and nums[right+1] == nums[right]:
                            right -= 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] <= target:
                        left += 1
                    else:
                        right -= 1
        return res
    