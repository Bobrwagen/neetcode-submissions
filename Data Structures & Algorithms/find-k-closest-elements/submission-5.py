class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = arr[:k]
        l = 0
        for i in range(k, len(arr)):
            dist = abs(arr[i] - x)
            distL = abs(arr[l] - x)
            if dist > distL:
                return res
            else:
                if dist < distL:
                    res = arr[l+1:l+k+1]
                l += 1
        return res
                