class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = 0
        right = 0
        res = ''
        while left < len(word1) or right < len(word2):
            if left < len(word1) and right < len(word2):
                res+=word1[left]
                res+=word2[right]
                left+=1
                right+=1
            elif left < len(word1):
                return res + word1[left:]
            elif right < len(word2):
                return res + word2[right:]
        return res