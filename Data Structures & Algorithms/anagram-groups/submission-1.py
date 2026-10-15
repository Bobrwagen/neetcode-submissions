class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs:
            tup = [0] * 26
            for c in string:
                ind = ord(c) - ord("a")
                tup[ind] += 1
            res[tuple(tup)].append(string)
        return list(res.values())