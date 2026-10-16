class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left and right iteration
        n = len(nums)
        pref = [1] * n
        suff = [1] * n
        for i in range(1, n):
            pref[i] = pref[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]
        return [suff[i] * pref[i] for i in range(n)]