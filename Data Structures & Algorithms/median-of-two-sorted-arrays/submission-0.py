class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
             return self.findMedianSortedArrays(nums2, nums1)
        
        m = len(nums1)
        n = len(nums2)
        half = (m+n) // 2
        l,r = 0, m - 1

        while True:
            i = (l+r) // 2
            j = half - i - 2
            Aleft = nums1[i] if i >= 0 else float("-infinity")
            Aright = nums1[i + 1] if (i + 1) < len(nums1) else float("infinity")
            Bleft = nums2[j] if j >= 0 else float("-infinity")
            Bright = nums2[j + 1] if (j + 1) < len(nums2) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if (m+n) % 2: 
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Bright, Aright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
