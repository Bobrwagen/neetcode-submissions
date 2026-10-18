class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        curr = set()
        res = 0
        while right < len(s):
            if s[right] in curr:
                while left < right:
                    curr.remove(s[left])
                    if s[left] == s[right]:
                        left += 1
                        break
                    left += 1
            curr.add(s[right])
            res = max(res, len(curr))
            right += 1
        return res