class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        vis = set()
        for n in nums:
            if n in vis:
                return n
            else:
                vis.add(n)
        return 0

        