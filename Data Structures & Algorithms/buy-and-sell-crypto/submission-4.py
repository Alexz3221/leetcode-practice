class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        buyPrice = prices[0]
        sellPrice = prices[0]
        for i in range(len(prices)):
            if prices[i] > sellPrice: sellPrice = prices[i]
            if prices[i] < buyPrice:
                buyPrice = prices[i]
                sellPrice = prices[i]
            profit = sellPrice - buyPrice
            if profit > max:
                print(buyPrice)
                print(sellPrice)
                max = profit

        return max