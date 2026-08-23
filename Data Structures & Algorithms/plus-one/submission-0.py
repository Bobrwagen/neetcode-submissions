class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        r = len(digits) - 1
        while carry == 1 and r >= 0:
            if digits[r] == 9:
                digits[r] = 0
                carry = 1
            else:
                carry = 0
                digits[r] += 1
            r -= 1
        if carry == 1:
            digits.insert(0,1)
        return digits
        