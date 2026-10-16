class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        currBuy = prices[0]
        currSell = prices[0]
        for i in range(1, len(prices)):
            currPrice = prices[i]
            if currPrice < currSell:
                res += currSell - currBuy
                currBuy = currSell = currPrice
            else:
                currSell = currPrice
        return res + currSell - currBuy
                
        