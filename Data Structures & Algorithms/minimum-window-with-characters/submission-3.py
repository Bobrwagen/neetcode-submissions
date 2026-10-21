class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = defaultdict(int), defaultdict(int)
        for c in t:
            countT[c] += 1
        
        have, need = 0, len(countT)
        res, resLen = [-1,-1], float("infinity")
        l = 0
        for i in range(len(s)):
            c = s[i]
            window[c] += 1
            if c in t and window[c] == countT[c]:
                have += 1
            while have == need:
                if i - l + 1 < resLen:
                    resLen = i - l + 1
                    res = [l, i+1]
                window[s[l]] -= 1
                if s[l] in t and window[s[l]] < countT[s[l]]:
                        have -= 1
                l += 1
        return s[res[0] : res[1]] if resLen else ""

