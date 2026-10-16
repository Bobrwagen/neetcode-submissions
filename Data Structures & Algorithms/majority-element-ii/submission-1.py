class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        res = []
        threshold = len(nums) // 3
        for k,v in counts.items():
            if v > threshold:
                res.append(k)
        return res