class Solution:
    def trap(self, height: List[int]) -> int:
        r = 0
        n = len(height)
        res = 0
        stack = []
        local = 0
        while r < n - 1:
            if height[r+1] < height[r]:
                stack.append([r,height[r]])
                local = 0
            elif height[r+1] > height[r]:
                while stack:
                    if height[r+1] == stack[-1][1]:
                        currX, currY = stack.pop()
                        y = min(currY, height[r+1]) - max(local,height[r])
                        x = r - currX
                        res += x * y
                        local = currY
                        if not stack:
                            local = 0
                        break
                    if height[r+1] > stack[-1][1]:
                        currX, currY = stack.pop()
                        y = min(currY, height[r+1]) - max(local,height[r])
                        x = r - currX
                        res += x * y
                        local = currY
                        if not stack:
                            local = 0
                    else:
                        currX, currY = stack[-1]
                        y = min(currY, height[r+1]) - max(local,height[r])
                        x = r - currX
                        res += x * y
                        local = 0
                        break
            r += 1
        return res
