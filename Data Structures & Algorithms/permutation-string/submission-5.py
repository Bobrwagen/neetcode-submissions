class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = defaultdict(int)
        n = len(s1)
        for c in s1:
            counts[c] += 1
        counter = defaultdict(int)
        l = 0
        for i in range(len(s2)):
            if s2[i] not in counts:
                l = i + 1
                counter.clear()
            else:
                counter[s2[i]] += 1
                while counter[s2[i]] > counts[s2[i]] or i - l + 1 > n:
                    counter[s2[l]] -= 1
                    l += 1
                if counter == counts:
                    return True
        return False