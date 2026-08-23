class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            char_tup = [0] * 26
            for c in s:
                ind = ord(c) - ord('a')
                char_tup[ind] += 1
            char_tup = tuple(char_tup)
            res[char_tup].append(s)

        return list(res.values())