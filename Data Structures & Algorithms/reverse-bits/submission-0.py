class Solution:
    def reverseBits(self, n: int) -> int:
        toRev = 0
        for i in range(32):
            toRev = toRev << 1
            toRev += (n&1)
            n = n >> 1
        return toRev
        