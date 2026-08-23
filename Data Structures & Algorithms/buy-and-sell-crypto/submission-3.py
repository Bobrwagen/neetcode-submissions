class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        res = [0,0]
        while i < len(prices) - 1:
            if  prices[i+1] > prices[i]:
                j = i + 1
                while j <= len(prices) - 1 and prices[j] > prices[i]:
                    res_prof = res[1] - res [0]
                    prof = prices[j] - prices[i]
                    if prof > res_prof:
                        res = [prices[i], prices[j]]
                    j += 1
                i = j
            else:
                i += 1
        return res[1] - res [0]