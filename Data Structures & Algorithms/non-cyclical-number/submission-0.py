class Solution:
    def isHappy(self, n: int) -> bool:
        contained = set()
        curr = n
        while curr != 1:
            curr = str(curr)
            tmp = 0
            for x in curr:
                a = int(x)
                tmp += a * a
            curr = tmp
            if curr in contained:
                return False
            contained.add(curr)
        return True
            
            
        