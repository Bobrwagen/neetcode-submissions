class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def binSearch(mountainArr, target, l, r):
            while l <= r:
                mid = (l+r) // 2
                num = mountainArr.get(mid)
                if num == target:
                    return mid
                elif num < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        #find Max
        l , r = 1, mountainArr.length() - 2
        lun = r + 2
        while l <= r:
            mid = (l+r) // 2
            num = mountainArr.get(mid)
            left = mountainArr.get(mid-1)
            right = mountainArr.get(mid+1)
            if left < num > right:
                l = mid
                break
            elif left < num < right:
                l = mid + 1
            else:
                r = mid - 1
        summit = l
        leftRes = binSearch(mountainArr, target, 0, summit)
        print(summit, leftRes)
        if leftRes == -1:
            l,r = summit + 1, lun-1
            while l <= r:
                mid = (l+r) // 2
                num = mountainArr.get(mid)
                if num == target:
                    return mid
                elif num < target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1
        return leftRes
        
        