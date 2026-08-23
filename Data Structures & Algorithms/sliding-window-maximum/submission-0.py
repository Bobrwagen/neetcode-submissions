class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        curr = -2000
        left = 0
        r = k-1
        while r < len(nums):
            if curr == -2000 or left == (r-k):
                curr = -2000
                for i in range(r-k+1,r):
                    if nums[i] > curr:
                        curr = nums[i]
                        left = i
            if nums[r] > curr:
                curr = nums[r]
                left = r
            res.append(curr)
            r +=1
        return res


            
        