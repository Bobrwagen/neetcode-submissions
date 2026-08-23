class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = []
        res = 0
        ctr = 0
        for ch in s:
            if ch in queue:
                ind = queue.index(ch)
                for i in range(ind+1):
                    queue.pop(0)
                    ctr -=1
            
            queue.append(ch)
            ctr +=1
            if ctr > res:
                res = ctr
        return res
        